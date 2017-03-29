# DLA Cluster
Python code for DLA cluster simulation and calculating fractal dimensionality of the cluster. 

<p align="center">
  <img src="/sampleImages/movie.gif" width="500">
</p>

## Cluster formation 
The movie (.gif) is a visual output for the DLA Cluster formation. In the beginning, a seed particle is added in the center. Then random walkers start at the specified radius from the center. They are added to the cluster if they reach it. If the random walker comes close to the edge of the field, it is removed. The cluster is considered complete once one of the cluster elements comes to the radius from which random walkers start.

To get this movie, you need to run file *runner.py*. To get different radius - vary the first parameter passed to the DLAcluster function. For example, this is a .gif file for a larger radius.

<p align="center">
  <img src="/sampleImages/movie_small.gif" width="500">
</p>


As we can see, the resulting cluster has a lot of holes and exhibits a branching behavior. This is understandable: if we add random walkers at the distance of the center and let them wander, there is a greater chance they will be added to the branches of the cluster as it grows.

 To quantify this observation, we can find the fractal dimensionality of the cluster. This parameters arises from the scaling rules: consider the mass of the objects. We can see that for a line mass is proportional to **r**, and for disk to **r<sup>2</sup>**. Therefore, consider expression 
 
<p align="center"> 
  log(m)=a log(r)+c 
</p>

Then, a is the power of r. For fractals, we would expect a value between 1 and 2. 

Indeed, running the DLA cluster for various radius, and finsing a fit through the points, we see that it is about 1.7
<p align="center">
  <img src="/sampleImages/fractalDim.png" width="500">
</p>


This result can be achieved by running *fractalDimensionality.py*

## Note
*Part of this code was used to complete the group assignment for Physics 566 (Computational Physics) class at Duke University, taught by Professor Steffen Bass. Team members: Ksenia Sokolova, Tahoe Schrader and Xinmeng Tong. The Github repository for the full assignment can be found [here](https://github.com/tahoeschrader/PHYS566_group4_project-1a_walk-diffusion-cluster)*

## Installing required packages
Most of the packages are easy to install through *pip install (package)*
However, installing *ffmpeg* for saving .gif requires a separate procedure. (Only needed if passed "True" for DLAcluster function)

For Mac users: install ffmpeg through homebrew
1. Install homebrew - folow the instructions on the [link](https://brew.sh)
(The password required is the computer password)
2. In the Terminal, type 
*brew install ffmpeg*
This will install it automatically



