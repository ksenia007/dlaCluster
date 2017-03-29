"""
This function finds the fractal dimensionality of the cluster 
"""

from DLAcluster import DLAcluster 
import numpy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit



radiusArray=numpy.arange(10,80,5)
mass=[]

for i in radiusArray:
    massValue,matrix=DLAcluster(i,False) #import radius and True/False for GIF
    mass.append(massValue)

#------- Find fit for mass and radius of the cluster:
# Find log radius and log mass
# Should be a linear function a+bx, with the slope b equal to the power of t and 'a'=scaling

#Find Log of all the arrays
logRadius=numpy.log(radiusArray)
logMass=numpy.log(mass)

#Fit a log function using numpy polyfit
fitLog=numpy.polyfit(logRadius, logMass,1)
fitLogFunc=numpy.poly1d(fitLog)

#print out the results
print("Parameters for the log fit: slope = ",fitLog[0],"shift: ",fitLog[1])
print("Parameters from the log fit: form is e^",fitLog[1],"*r^",fitLog[0])
num=str(numpy.round(fitLog[0],3))

# ------------------------------------------------------------------------------

################################################################################
### Create Plots
################################################################################

# ------------------------------------------------------------------------------

#--------------- Plot log
fig=plt.subplot()
plt.scatter(logRadius,logMass, color='tomato', edgecolors='tomato', s=30)
plt.plot(logRadius, fitLogFunc(logRadius),color='dodgerblue', lw=3)
plt.title("Log-log plot, mass vs radius",fontsize=20)
plt.xlabel("Log radius",fontsize=15)
plt.ylabel("Log mass",fontsize=15)
plt.grid(True)
fig.text(2.6,4.3,'fractal dimensionality:'+num)
fig.spines["top"].set_visible(False)  
fig.spines["right"].set_visible(False)  
plt.savefig('logRadiusMass.png')
plt.show()


