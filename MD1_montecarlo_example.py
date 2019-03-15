# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 18:39:39 2018

@author: pmzyl
"""

import numpy as np
import matplotlib.pyplot as plt
import pylab

popul = 5
K = 1.4 #this is the service speed
Nsteps = 1000
Qsize = np.zeros(Nsteps) #array to track the state of the queue

IAtimes = np.random.exponential(1,popul) ###generate inter-arrival times of customers with whatever distribution you like
###here it is for 10 customers, each inter-arrival is an exponential with rate 1.
print('Interarrival times: {}'.format(IAtimes))
Atimes = np.cumsum(IAtimes) ###these are the "real" arrival times
print('Arrival times: {}'.format(Atimes))
Tmax = np.ceil(Atimes[-1]) ###set max simulation time
print('Total time of a queue: {}'.format(Tmax))

####discretize time
t = np.linspace(0,Tmax,Nsteps)
dt = t[2] - t[1] #this is the unit of service time


##understand index of arrival
Aindex = (np.ceil((Atimes/Tmax)*Nsteps))
print('Indexes of arrivals out of Nsteps = {}: {}'.format(Nsteps, Aindex))

####simulate queue
for i in range(Nsteps-1):
    Qsize[i+1] = Qsize[i] + np.max(((t[i] - Atimes)<0) * ((t[i+1] - Atimes )>0))
    Qsize[i+1] = max(0,Qsize[i+1] - K*dt)

## understand what is a size and a time of a queue when arrives
QsizeArr = np.zeros(popul)
QtimeArr = np.zeros(popul)

for i in range(0, len(Aindex)):
    QsizeArr[i] = Qsize[int(Aindex[i])]

QtimeArr = QsizeArr * K
AvrgtimeArr = np.mean(QtimeArr)

print('Size of a queue for a new arrival: {}'.format(QsizeArr))
print('Time in a queue for a new arrival: {}'.format(QtimeArr))
print('Average time in a queue: {}'.format(AvrgtimeArr))

realQ = np.ceil(Qsize) ###this rounds up so we have integer customers

plt.figure(1)
plt.plot(Atimes) #plot arrival times
plt.figure(2)
plt.plot(t,realQ) #plot the state of the queue

pylab.show()
