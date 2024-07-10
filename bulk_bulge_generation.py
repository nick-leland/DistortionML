import numpy as np
from PIL import Image
from transformation import apply_vector_field_transform
import os
from os import path

def definitions(generator):

    # The image bulge should be entirly contained within the image.  For instance, if we have a radius of 0.5 (the max), the image should be force to be at 0.5 (x and y) locations.
    # radius = generator.random() * 0.5
    radius = generator.normal(loc=0.25, scale=(0.5/6))
    # print(f"Radius is {radius}")
    # strengtH = Generator.random()
    strength = generator.normal(loc=1, scale=(1/6))
    # print(f"Strength is {strength}")

    smoothness = generator.normal(loc=1, scale=(1/6))
    # print(f"Smoothness is {smoothness}")

    # size = 3
    
    vmin = min([1-radius, radius])
    vmax = max([1-radius, radius])
    print()
    print("Radius is {radius}")
    print("Max and Min positions to calculate mean + std")
    print(vmin)
    print(vmax)
    print()
    
    print("Mean and Std Dev")
    mean = (vmax+vmin) / 2
    std = (vmax-vmin) / 4
    print(mean)
    print(std)
    print()
    # x = generator.normal(loc=mean, scale=std, size=(2))
    x = np.random.uniform(low=vmin, high=vmax, size=(2))
    # print(x)
    
    # print(f"({np.random.uniform(vmin, vmax)}, {np.random.uniform(vmin, vmax)})")
    # print(f"({x[0]}, {x[1]})")
    return radius, x, strength, smoothness

def smooth(generator, strength):
    # edge
    emaxval, eminval = 0.75, 0.25
    emean = (emaxval + eminval) / 2
    estd = (emaxval - eminval) / 6

    # center
    cmaxval, cminval = 0.5, 0.25
    cmean = (cmaxval + cminval) / 2
    cstd = (cmaxval - cminval) / 4


    edge = generator.normal(loc=emean, scale=estd)
    center = generator.normal(loc=cmean, scale=cstd)

    return edge, center

def bulge(x, y):
    return -np.sqrt(x**2 + y**2)

if __name__ == "__main__":
    # Sets the numpy generator
    rng = np.random.default_rng()

    os.makedirs("data", exist_ok=True)
    os.chdir("data/")
    os.makedirs("grid", exist_ok=True)
    os.makedirs("output", exist_ok=True)
    files = os.listdir("grid/")
    os.chdir("grid/")

    for _ in files:
        rad, location, strth, smth = definitions(rng)
        I = np.asarray(Image.open(_))
        transformed, (gx, gy) = apply_vector_field_transform(I, bulge, rad, location, strth, smth)

        os.chdir("../output/")
        result = Image.fromarray(transformed)
        result.save(f"{_.title()}.jpg")
        os.chdir("../grid/")


