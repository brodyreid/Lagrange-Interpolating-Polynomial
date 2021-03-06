# Returns the Lagrange interp polynomial given xdat and ydat

import numpy as np
import matplotlib.pyplot as plt
import random as rand

# Define langrange pieces L_i
def L(i,x,xdat):
    l = 1
    for k in range(0,len(xdat)):
        if k != i:
            l *= (x-xdat[k])/(xdat[i]-xdat[k])
    return l

# Define polynomial P(x)
def lagrange_interp(x,xdat,ydat):
    P = 0
    for i in range(0,len(xdat)):
        P += ydat[i]*L(i,x,xdat)
    return P

def f(x):
    return 1/(1 + 4 * np.power(x,2))

# Compute f(x) at a bunch of x values (to make a smooth curve) and plot it on interval [-2,2]
x = np.linspace(-2,2,51)
y = f(x)
plt.plot(x,y)

# Make a list of points including -2, 2, and 6 random values in [-2,2]
# I'm trusting that there will not be repetition between the random values
xdat = [2, -2]
for i in range(0,6):
    xdat.append(rand.uniform(-2,2))
print('randomly generated x values for interpolation are:\n %s' %(xdat))

# Plot the points (xdat,f(xdat)) that we're going to interpolate
ydat = f(xdat)
plt.scatter(xdat,ydat)

# Compute the interpolating polynomial at a bunch of x values and plot it
P = []
for xx in x:
    P.append(lagrange_interp(xx,xdat,ydat))
plt.plot(x,P)
