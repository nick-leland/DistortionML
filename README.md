# Distortion ML
A project about the creation and deployment of a Machine Learning Model to first recognize and then reverse image distortions.

# What is it?
The goal of this project is to work on model creation and fine tuning.  The end result is a deployable machine learning model that detects if an image has had any distortional effects applied to it, and then attempts to reverse those effects.  

Take a look at the image below for a better example of this process. First we will use a classification model to determine if any distortional effects are actually taking place.  After this occurs, we can then run the distortion model on the image to attempt to reverse any distortional effects.  
<p align="center">
<img width="909" alt="shapes at 24-06-19 15 03 19" src="https://github.com/nick-leland/DistortionML/assets/148659884/0fd16956-dae7-404f-8fa2-e030e0a4339f">
</p>

<img align="right" src="https://github.com/nick-leland/DistortionML/assets/148659884/7948caf6-c276-44f5-a56a-61654f9f873d">
&emsp;The inspiration for this project was found when I was initially working on a project to generate images of mazes for use in machine learning.  One blog that I read discussed that you could then apply image manipulation techniques on the mazes to increase the mazes difficulty.  This utilized a simple map effect where you would map an image onto a circle.  I am working on a tool that will apply image distortion based on something like a contour map of a gradient.  My goal is to train the model on what distortion techniques are used based on the input of an image.  Once it can accurately predict the equation, the program would apply the inverse to restore the image.  



&emsp;I read about a direct use case where software was used to reverse an image transformation to identify a criminal.  The criminal used a spiral effect to distort his face and attempt to hide behind anonyminity.  The goal is to produce a tool that will do something similar using machine learning techniques.  

## How will this be achieved? 
This project will be broken down into various different portions.
1. Generate an initial dataset that can be used for classification trianing
2. Create a program that will randomly apply distortion effects to images
3. Apply these distortion effects to a subset of images that increase with difficulty.  The current plan is to go from Grids -> Mazes -> Photos.  Will likely need redefining later.
4. Look into deployment for hosting the model.
5. Allow for users to apply the distortional effects themselves, and then directly apply the model to them after.
6. Web deployment of user effects.

## Stack
This is a Python project, many things will take place within python scripts and jupyter notebook files (although I much prefer base python scripts). 
I will be working primarily with Numpy and Pytorch, but would also like to begin to work with JAX as well.  I am still very much in the early phases of ML understanding so there will be many novice aspects to this project.

## Made for Summer of Shipping / Nights and Weekends via Buildspace!
<p align="center">
<img width="909" alt="shapes at 24-06-19 15 03 19" src="https://github.com/nick-leland/DistortionML/assets/148659884/a7dea974-37dc-41c2-af58-923cbe4012ef">
</p>
