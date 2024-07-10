import numpy as np
from PIL import Image
import os
from os import path
from transformation import apply_vector_field_transform
from dfs_generation import generate
from img_gen import init, run

if __name__ == "__main__":
    # Creates the generator
    rng = np.random.default_rng()

    # Sets our main directory
    os.makedirs("data", exist_ok=True)
    os.chdir("data/")

    # Create output directory and move to the maze output
    os.makedirs("maze", exist_ok=True)
    os.makedirs("distorted", exist_ok=True)
    os.chdir("maze/")

    # Base parameters
    size_x = 25
    size_y = 25
    walls = 3
    cell = 15
    x = int(input("How many pictures would you like to generate?"))

    # Generate initial grid
    # Removed the max_y from init
    # a = init(size_x, size_y, walls, cell, max_y)
    a = init(size_x, size_y, walls, cell)


    for _ in range(x):
        path, neighbors = generate(size_x, size_y)

        # Generate maze from grid
        maze = run(path, neighbors, cell, walls, size_x, size_y, name=_, in_array=a, save=False, return_array=True)


        os.chdir("distorted/")
        transformed , (gx, gy) = apply_vector_field_transform(I, bulge, rad, location, strength, smooth)

        os.chdir("../distorted/")
        result = Image.fromarray(transformed)
        result.save(f"{_.title()}.jpg")
        os.chdir("../maze/")


        
