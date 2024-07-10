import os
import numpy as np
from os import path
from dfs_generation import generate
from img_gen import init, run
from PIL import Image


# Overall Parameters
# Overall image size: 16x9 Aspect Ratio

# Target image size should be around this? 

def maze_grid_generation(size_x, size_y, walls, cell, max_y, counter, gridonly=False, mazeonly=False):
    """Creates mazes and grids that both match a range of pixel prospects"""
    # Creates a folder for the type of data it's generating 
    # In this case Mazes and Grids which will use the same pixel information
    path, neighbors = generate(size_x, size_y)
    a = init(size_x, size_y, walls, cell, max_y)

    # Save pictures to the database
    grid = Image.fromarray(a)
    grid = grid.convert('RGB')
    if mazeonly == False: 
        os.makedirs("grid", exist_ok=True)
        grid.save(f"grid/{size_x}_x_{size_y}_{walls}_{cell}g.jpg")
        return a
    # grid.show()

    if gridonly == False:
        run(path, neighbors, cell, walls, size_x, size_y, max_y, in_array=a, save=False)

        maze = Image.fromarray(a)
        maze = maze.convert('RGB')
        os.makedirs("maze", exist_ok=True)
        maze.save(f"maze/{size_x}_x_{size_y}_{walls}_{cell}_{counter}m.jpg")
        # maze.show()
        return a
        


# Image generation should be configured, now just need to setup the maze generation
if __name__ == "__main__":

    os.makedirs("data", exist_ok=True)
    os.chdir("data/")

    combinations = {}
    ratio_x, ratio_y = 16, 9
    target_x, target_y = 1280, 720

    # We increased to 750/650 to create more mazes.

    max_y = 750
    # min_y = 727
    min_y = 650
    # Target is 720, range of + 14 pixels
    tolerance = max_y - target_y
    
    # Figure out max padding?
    # Maybe there is a better way to mathematically calculate this value
    # This is used to find the min and max of y
    # max_y = 0
    # min_y = float('inf')
    # print("Finding the max length for the y value of the pixel")
    # for _ in range(1, int((target_x / ratio_x)+1)):
    #     pixel_combinations = [(9 * cell_size + (9+1) * wall_size) for cell_size in range(1, 100000) for wall_size in range(1, 100) if (16 * cell_size + (16 + 1) * wall_size) == 1280 and cell_size > wall_size]
    #     if max(pixel_combinations) > max_y:
    #         max_y = max(pixel_combinations)
    #     if min(pixel_combinations) < min_y:
    #         min_y = min(pixel_combinations)
    # print("Search completed")
    # print(f"max_y is {max_y}")
    # print(f"min_y is {min_y}")
    

    def size(size, cell, wall):
        result = (size * cell + (size + 1) * wall)
        return result

    runs = int(input("How many times would you like to generate a maze of each size?"))

    total_cycles = target_x // ratio_x

    for _ in range(total_cycles):
        size_x = 16 * (_+1)
        size_y = int((size_x * 9) / 16)
        print(size_x, size_y)

        print("running")
        search = 1000
        max_size = target_x + tolerance
        pixel_combinations = [[cell_size, wall_size] for cell_size in range(1, search) for wall_size in range(1, search) if size(size_x, cell_size, wall_size) > target_x and size(size_x, cell_size, wall_size) < max_size and cell_size > wall_size]

        print(pixel_combinations)
        counter = 0

        for combo in pixel_combinations:
            combinations.update({counter: [size_x, size_y, combo[1], combo[0]]})
            counter += 1
    # First need to locate the folder for where the data will go

    print(combinations)
    count = 0
    r = len(combinations.keys())

    # For troubleshooting
    y = list(combinations.keys())
    y.reverse()
    for _ in y:
    # for _ in combinations.keys():
        for x in range(runs):
            print(f"Making a maze with the following:\nX Size = {combinations[_][0]}\nY Size = {combinations[_][1]}\nWall Size = {combinations[_][2]}\nCell Size = {combinations[_][3]}")
            # I'm thinking of reformating this to instead be within the above loop.
            maze_grid_generation(combinations[_][0], combinations[_][1], combinations[_][2], combinations[_][3], max_y, x, gridonly=True)
            print(f"""Generated Maze-Grid '{combinations[_][0]}_x_{combinations[_][1]}_{combinations[_][2]}_{combinations[_][3]}.jpg'""")


