"""
This function runs the code from DLAcluster
"""

from DLAcluster import DLAcluster 


#### NOTE: input to the function is (RADIUS, needGif), where 
# need gif defines whether the .gif for the cluster is created

#### NOTE 2: .gif creation takes a lot of space: first images are saved one by one, 
# then collapsed into the .gif, and intermediate files are deleted.
# Large radius results in large .gif file 

#### NOTE 3: folder "/images" is created if not present, and final cluster image is always saved

#### NOTE 4: radius>100 takes some time to run. Gif files are relatively large in this case

mass,matrix=DLAcluster(90,True) #import radius and True/False for GIF

