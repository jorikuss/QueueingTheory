# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pylab

size = 10
N = 100
lmbd = 3.0
spd = 1. ##service speed
dt = spd/N

Tmax = 10.

#def EuMeth(size, N, lmbd):

t = np.arange(0, Tmax, dt) ##
Nsteps = len(t)

P = np.zeros((size*N + 1, Nsteps)) ##2-d P(t)
P[0,0] = 1
dP = np.zeros(size*N + 1) ## 2-d dP/dt

#    """Defining M, such that diagonals: +lambda, and diagonal + N: -lambda :"""

M = np.zeros((size*N + 1, size*N + 1)) ##2-d with distributions
np.fill_diagonal(M, -1)
for i in range(N*size + 1):
    if (i+N) <= (N*size):
        M[i,i+N] = 1
    else:
        M[i,i] = 0

plt.figure(1)
plt.imshow(M)

#    """Defining firts row of dP"""
    ## dP[:,0] = lmbd * (-P[:,0] + np.matmul(M, P[:,0]))

#    """Applying Euler's method to find P"""
for j in range(Nsteps-1):
    dP = dt * lmbd * (np.dot(M.transpose(), P[:,j]))
    P[:,j+1] = P[:,j] + dP


    j1 = P[0,j+1]
    P[:,j+1] = np.roll(P[:,j+1], -1)
    P[0,j+1] = P[0,j+1] + j1
    P[-1,j+1] = 0

allP = np.zeros((size+1, Nsteps))


allP[0,:] = P[0,:]
for j in range(size):
    allP[j+1,:] = np.sum(P[j*N+1:(j+1)*N,:], axis=0)


plt.figure(2)
plt.plot(P[5,:])

plt.figure(3)

for i in range(size):

    plt.plot(allP[i,:])

pylab.show()


    #

    #print('P over t:\n {}'.format(P))

    ## print('dP/dt over t:\n {}'.format(dP))


#EuMeth(2, 3, 0.5)
