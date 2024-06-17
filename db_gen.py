import os
import numpy as np
from os import path
from gen import generate
from img_gen import init, run
from PIL import Image


# Overall Parameters
# Overall image size: 16x9 Aspect Ratio

# Target image size should be around this? 

def maze_grid_generation(size_x, size_y, walls, cell):
    """Creates mazes and grids that both match a range of pixel prospects"""
    # Creates a folder for the type of data it's generating 
    # In this case Mazes and Grids which will use the same pixel information
    path, neighbors = generate(size_x, size_y)
    a = init(size_x, size_y, walls, cell)
    
    # Save pictures to the database
    grid = Image.fromarray(a)
    grid = grid.convert('RGB')
    path = os.path.relpath("data/grid")
    grid.save(f"{size_x}_x_{size_y}_{walls}_{cell}g.jpg")

    run(path, neighbors, cell, walls, size_x, size_y, in_array=a, save=False)

    maze = Image.fromarray(a)
    maze = maze.convert('RGB')
    path = os.path.relpath("data/maze")
    maze.save(f"{size_x}_x_{size_y}_{walls}_{cell}m.jpg")


# Image generation should be configured, now just need to setup the maze generation
if __name__ == "__main__":
    #Target Size for Images
    x, y = 1280, 720

    # Using this as minimum to keep aspect ratio
    min_combo_x, min_combo_y = 2, 1
    # Formula for maximum cells ((x-1)/2)
    max_combo_x, max_combo_y = 640, 360



    
    combinations = {}
    rng = np.random.default_rng()


    combo_count = int(input("How many images would you like to generate?"))
    for _ in range(combo_count):
        # Uses the min and max values to generate the size
        size_x = rng.integers(low=min_combo_x, high=max_combo_x)
        size_y = rng.integers(low=min_combo_y, high=max_combo_y)

        if size_x < size_y:
            temp = size_x
            size_x = size_y
            size_y = temp
            cell_count = size_x
        else:
            cell_count = size_x

        # This formula is the one drawn in tldraw
        # max_x = ((x-(cell_count+1)*wall_size)/cell_count)
        max_x = ((x-(cell_count+1)*1)/cell_count)
        # max_y = ((x-(cell_count*cell_size))/cell_count+1)
        max_y = ((x-(cell_count*1))/cell_count+1)

        min_x, min_y = 1, 1
        size_cell = rng.integers(low=min_x, high=max_x)
        size_wall = rng.integers(low=min_y, high=max_y)

        combinations.update({_ : [size_x, size_y, size_wall, size_cell]})




    # First need to locate the folder for where the data will go

    count = 0
    r = len(combinations.keys())
    for _ in combinations.keys():
        print(f"Making a maze with the following: {combinations[_][0]}, {combinations[_][1]}, {combinations[_][2]}, {combinations[_][3]}")
        # I'm thinking of reformating this to instead be within the above loop.
        maze_grid_generation(combinations[_][0], combinations[_][1], combinations[_][2], combinations[_][3])
        print("Generated Maze-Grid {size_x}_x_{size_y}_{walls}_{cell}")



