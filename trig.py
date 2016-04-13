#!/usr/bin/python

# The following statements are used to import numpy and matplotlib.
import numpy as np
import matplotlib.pyplot as plt

# TODO fill in this function
def integrate(y, dx):
    integral=(np.sum(y))*dx
    return integral

# TODO write code here to setup arrays x and y = sin(x) and then plot them.
# After this is done implement your integrate function above integrate y

#Integrates sin(x) from 0 to pi
x=np.arange(0, np.pi, 0.01)
y=np.sin(x)
plt.plot(x,y)
plt.show()
Sum1=integrate(y, 0.01)
print Sum1

#Integrates cos(x) from 0 to pi
z=np.cos(x)
plt.plot(x,z)
plt.show()
Sum2=integrate(z, 0.01)
print Sum2
        
#Numerically integrates using Numpy's trapezoidal rule
Trap1=np.trapz(y, x=None, dx=0.01)
print Trap1
Trap2=np.trapz(z, x=None, dx=0.01)
print Trap2