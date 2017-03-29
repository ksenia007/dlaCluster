"""
This is the main funciton for the DLA cluster model. 
INPUT: RADIUS (Integer), needGif (Boolean)
OUTPUT: # of particles in the cluster (int), resulting matrix (populated by 0, 1, 2)
SAVED OUTPUT: in the folder images saves the resulting cluster image and .gif file
    -note: if folder images does not exist, it is created first
"""


import random
import numpy
import matplotlib.pyplot as plt
import os
from matplotlib import colors



############ Custom functions
from checkAround import checkAround
from randomAtRadius import randomAtRadius
#from indexM import indexM
############


def DLAcluster(radius, needGif):
    
    #check if folder "images" exists, and if not - create it
    if not os.path.isdir("images"):
        os.mkdir("images")
    
    if needGif:
        #Import there libraries if intend to save gif
        #NOTE: need imageio package, and ffmpeg. Refer to readme for more info
        import imageio

    
    #initialize variables that are dependent upon the radius
    # note - we add 2 to the parameters to get a thick broder between the edges of the disk and square
    # x coordinate of a seed particle
    seedX = radius+2 
    # y coordinate of a seed
    seedY = radius+2 
    # size of the grid to account for field of wandering around
    squareSize = radius*2+5

    matrix=numpy.zeros((squareSize, squareSize))

    for row in range (0,squareSize):
        for col in range (0,squareSize):
            #put a seed particle
            if row==seedY and col==seedX: 
                matrix[row][col]=1
            #define field outside of circle
            elif numpy.sqrt((seedX-col)**2+(seedY-row)**2)>radius:
                matrix[row][col]=2
    cmap = colors.ListedColormap(['navy','white', 'navy'])

    # Initialize the random walker counter
    randomWalkersCount = 0

    # Set the cluster to NOT be complete
    completeCluster = False

    # Start running random walkers
    addedCount=0 #keep track of number added

    # initialize array for the used interval for graphing
    usedInterval=[]

    while not completeCluster:
        # Release a walker
        randomWalkersCount += 1
        random.seed()

        # Generate a (Xstart, Ystart) for walker, need within radius
        location=randomAtRadius(radius, seedX, seedY)

        # Initialize variables, like Friend tag and near edge identifier
        foundFriend = False #not near other particle
        nearEdge=False #not near the edge of the field


        # Set an individual walker out, stop if found a 'friend', give up if it reached the edge of the board
        while not foundFriend and not nearEdge:
            # Run the checking/walking function
            locationNew,foundFriend, nearEdge, exitCircle = checkAround(location,squareSize,matrix)

            # Add to the cluster if near a friend
            if foundFriend:
                # current location, replace with 1 and stop
                matrix[location[1]][location[0]] = 1
                addedCount+=1

            # Otherwise, save the location
            else:
                location = locationNew
        
        #print update 
        intervalSavePic=range(2,400000,500)
        if randomWalkersCount in intervalSavePic:
            print("still working, have added ", randomWalkersCount, " random walkers.", " Added to cluster: ", addedCount)
        if needGif:
            if randomWalkersCount in intervalSavePic:
                print("save picture")
                usedInterval.append(randomWalkersCount) #append to the used count
                label=str(randomWalkersCount)
                plt.title("DLA Cluster", fontsize=20)
                plt.matshow(matrix, interpolation='nearest',cmap=cmap)#plt.cm.Blues) #ocean, Paired
                plt.xlabel("direction, $x$", fontsize=15)
                plt.ylabel("direction, $y$", fontsize=15)
                plt.savefig("images/cluster{}.png".format(label), dpi=200)
                plt.close()
       
        if randomWalkersCount==400000:
            print("CAUTION: had to break the cycle, taking too many iterations")
            completeCluster = True

        # Once it finds a friend and leaves the previous loop, we must check if it
        # is also touching a circular wall. If so, we have a complete cluster
        if foundFriend and exitCircle:
            print("Random walkers in the cluster: ",addedCount)
            completeCluster = True
    
    plt.title("DLA Cluster", fontsize=20)
    plt.matshow(matrix, interpolation='nearest',cmap=cmap)#plt.cm.Blues) #ocean, Paired
    plt.xlabel("direction, $x$", fontsize=15)
    plt.ylabel("direction, $y$", fontsize=15)
    plt.savefig("images/cluster.png", dpi=200)
    plt.close()

    print(usedInterval)

    if needGif:
        with imageio.get_writer('images/movie.gif', mode='I') as writer:
            for i in usedInterval:
                filename="images/cluster"+str(i)+".png"
                image = imageio.imread(filename)
                writer.append_data(image)
                os.remove(filename)
            image = imageio.imread("images/cluster.png")
            writer.append_data(image)

    return addedCount, matrix

