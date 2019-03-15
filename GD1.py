# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 18:39:39 2018

@author: pmzyl & pmygi1 @nottingham.ac.uk
"""

import numpy as np
import matplotlib.pyplot as plt
import pylab

k = 2

trials = 100 #number of simulations
size = 10 #size of a queue
x
Nsteps = 1000 #this is x-axisk
S = 1 #this is the service speed


Qsize = np.zeros((trials, Nsteps)) ## matrix of outcomes

## understand what is a size and a time of a queue when arrives
QsizeArr = np.zeros((trials, size))
QtimeArr = np.zeros((trials, size))
QsizeAvrArr = np.zeros(trials)
QtimeAvrArr = np.zeros(trials)

QavrT = np.zeros(Nsteps)

Tmax = 40
t = np.linspace(0, Tmax, Nsteps)
dt = t[2] - t[1] #this is the unit of service time

for i in range (0, trials):

    IAtimes = np.random.exponential(k, 1000) ### gamma distribution with shape, scale
    print('Interarrival times: {}'.format(IAtimes))
    Atimes = np.cumsum(IAtimes) ###these are the "real" arrival times
    print('Arrival times: {}'.format(Atimes)) ##understand index of arrival
    Aindex = (np.ceil((Atimes/Tmax)*Nsteps))
    print('Indexes of arrivals out of Nsteps = {}: {}\n'.format(Nsteps, Aindex))


    ####simulate queue
    for j in range(Nsteps-1):

        Qsize[i, j+1] = Qsize[i, j] + np.max(((t[j] - Atimes)<0) * ((t[j+1] - Atimes )>0))
        if Qsize[i, j+1] > size:
            Qsize[i, j+1] = Qsize[i, j+1] - 1

        Qsize[i, j+1] = max(0,Qsize[i, j+1] - S*dt)


realQ = np.ceil(Qsize) ###this rounds up so we have integer customers

print('Explicit size of a queue is\n {}'.format(Qsize))
print('\n')

'''for i in range (0, trials):
    for j in range(0, len(Aindex)):
        QsizeArr[i, j] = Qsize[i, int(Aindex[j])]
        QtimeArr[i, j] = QsizeArr[i,j] * S
    QsizeAvrArr[i] = np.mean(QsizeArr[i,])
    QtimeAvrArr[i] = np.mean(QtimeArr[i,])
'''
QavrT = np.mean(Qsize, axis = 0)

##print(QsizeAvrArr)
print('Average waiting in a queue for a new:\n {}'.format(QtimeAvrArr))
print('\n')
print('Average waiting in a queue over T:\n {}'.format(QavrT))
print('\n')

plt.figure(1)
plt.plot(t, QavrT) #plot arrival times
pylab.show()
'''
    plt.figure(2)
    plt.plot(Atimes)
    plt.figure(3)
    plt.plot(t,realQ) #plot the state of the queue
    pylab.show()
'''
