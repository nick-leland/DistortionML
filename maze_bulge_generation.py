import numpy as np
from PIL import Image
import os
from os import path
from transformation import apply_vector_field_transform
from dfs_generation import generate
from img_gen import init, run

if __name__ == "__main__":
    rng = np.random.default_rng()

    os.makedirs("data", exist_ok=True)
    os.chdir("data/")
    os.makedirs("distorted", exist_ok=True)
    os.makedirs("output", exist_ok=True)
    files = os.listdir("maze/")
    os.chdir("maze/")

    # Parameters
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

        transformed , (gx, gy) = apply_vector_field_transform(I, bulge, rad, location, strength, smooth)

        os.chdir("../distorted/")
        result = Image.fromarray(transformed)
        result.save(f"{_.title()}.jpg")
        os.chdir("../maze/")


        
