"""
This functions checks the initial locations, to make sure it is not at the edge of the square. 
If not at the edge:
checks the perimeter (up, down, left, right). The boolean variables foundFriend, exitCircle, nearEdge
are then assigned as TRUE, if they are true.
If the particle is not next to the other, and not at the edge of the square the new location is defined

PARAMETERS:
INPUT = location, in form [X,Y]
OUTPUT = new location ([X,Y]), foundFriend (BOOLEAN), nearEdge (BOOLEAN), exitCircle(BOOLEAN)

"""
import random 

def checkAround(location,squareSize,matrix):
	foundFriend = False #found another particle
	exitCircle = False #reached the required radius
	nearEdge=False #near the edge of the field
	
	
    # Check if a walker is near the edge
	if (location[1] + 1) > squareSize - 1 or (location[1] - 1) < 1 or (location[0] + 1) > squareSize - 1 or (location[0] - 1) < 1:
		nearEdge = True

    # If not near the edge, check if the walker is near a neighbor or reached the required radius
    # location[1]=row, location[2]=column
	if not nearEdge:
		neighborDown = matrix[location[1]+1,location[0]]
		if neighborDown == 1:
			foundFriend = True
		if neighborDown == 2:
			exitCircle = True

		neighborUp=matrix[location[1]-1,location[0]]
		if neighborUp==1:
			foundFriend=True
		if neighborUp==2:
			exitCircle=True

		neighborRight=matrix[location[1],location[0]+1]
		if neighborRight==1:
			foundFriend=True
		if neighborRight==2:
			exitCircle=True

		neighborLeft=matrix[location[1],location[0]-1]
		if neighborLeft==1:
			foundFriend=True
		if neighborLeft==2:
			exitCircle=True

    # After checking locations, if locations are good, start the random walk
	if not foundFriend and not nearEdge:
		decide = random.random()
		if decide<0.25:
			location = [location[0] - 1,location[1]]
		elif decide<0.5:
			location = [location[0] + 1,location[1]]
		elif decide<0.75:
			location = [location[0],location[1] + 1]
		else:
			location = [location[0],location[1] - 1]

	return (location, foundFriend, nearEdge, exitCircle)