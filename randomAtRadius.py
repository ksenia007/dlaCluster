"""
Function the generates the random location, at the specified radius
INPUT = radius, seedX, seedY
OUTPUT = [x,y] location
"""

import random
import numpy

def randomAtRadius(radius, seedX, seedY):
    theta = 2*numpy.pi*random.random() #generate random theta
    x=int(radius*numpy.cos(theta))+seedX #use trig to transfer into X
    y=int(radius*numpy.sin(theta))+seedY #find Y coordinate
    location=[x, y] #save locaction
    return location