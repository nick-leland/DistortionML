import numpy as np
from PIL import Image
import os
from os import path
from transformation import apply_vector_field_transform
from dfs_generation import generate
from bulk_bulge_generation import definitions
from img_gen import init, run


def yolo_output(obj_id, x, y, w, h, all_ids):
    if len(str(obj_id)) > len(str(max(all_ids))):
         spaces = " " * len(str(max(all_ids))) - len(str(obj_id))
    else:
         spaces = ''
    
    return f"{obj_id}{spaces} {x} {y} {w} {h}"


if __name__ == "__main__":
    # Creates the generator
    rng = np.random.default_rng()

    # We want to create one dataset where we use mazes and bulge the same mazes, and one where we use different mazes.

    # Sets our main directory
    os.makedirs("data", exist_ok=True)
    os.chdir("data/")

    os.makedirs("labels", exist_ok=True)
    os.chdir("labels/")

    os.makedirs("maze", exist_ok=True)
    os.makedirs("fresh_maze", exist_ok=True)
    os.makedirs("distorted", exist_ok=True)
   

    os.makedirs("images", exist_ok=True)
    os.chdir("images/")

    # Create output directory and move to the maze output
    os.makedirs("maze", exist_ok=True)
    os.makedirs("fresh_maze", exist_ok=True)
    os.makedirs("distorted", exist_ok=True)

    # We first save a fresh maze so prep that location 
    os.chdir("fresh_maze/")

    # Base parameters
    size_x = 25
    size_y = 25
    walls = 3
    cell = 15
    x = int(input("How many pictures would you like to generate?"))


    # Defines the bulge function we will be using
    def bulge(x, y):
        r = -np.sqrt(x**2 + y**2)
        return r 

    # Generate initial grid
    # Removed the max_y from init
    # a = init(size_x, size_y, walls, cell, max_y)


    # Sets the information that the yolo_output will use
    label = 0
    YOLO_dict = {0 : 'Bulge'}
    ids = list(YOLO_dict.keys())


    for _ in range(x):
        print(f"{_}/{x}")
        # Generates grids for the initial maze creation
        a = init(size_x, size_y, walls, cell)
        b = init(size_x, size_y, walls, cell)

        path, neighbors = generate(size_x, size_y)
        path_fresh, neighbors_fresh = generate(size_x, size_y)

        # Creates and saves a fresh maze
        fresh_maze = run(path_fresh, neighbors_fresh, cell, walls, size_x, size_y, name=f"{_}_fresh", in_array=b, save=True, return_array=True)

        os.chdir("../maze/")
        # Generate maze from grid
        maze = run(path, neighbors, cell, walls, size_x, size_y, name=f"{_}_maze", in_array=a, save=True, return_array=True)

        os.chdir("../distorted/")

        radius, location, strength, edge_smoothness= definitions(rng)
        center_x = location[0]
        center_y = location[1]
        print()
        print("Location (x, y)")
        print(f"({center_x}, {center_y})")
        print()

        # Using a 0 smooth in order to add harsh values
        edge_smoothness = 0
        center_smoothness = 0

        transformed , (gx, gy) = apply_vector_field_transform(maze, bulge, radius, (center_x, center_y), strength, edge_smoothness, center_smoothness)

        transformed_out = Image.fromarray(transformed)
        transformed_output = transformed_out.convert('RGB')
        transformed_out.save(f"{_}_distorted.jpg")


        
        size = radius * 2
        print(yolo_output(label, center_x, (1-center_y), size, size, ids))


        result = Image.fromarray(transformed)
        os.chdir("../fresh_maze/")

