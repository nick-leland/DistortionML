import os
import sys
import numpy as np
from PIL import Image
import time

sys.path.append('../')
# from dataset_generation import img_gen 
from img_gen import run

# from dataset_generation import dfs_generation
from dfs_generation import generate


if __name__ == "__main__":
    size = input("What size of a maze do you want? Required format is '#x#'")
    size = size.split("x") 
    sizex = int(size[0])
    sizey = int(size[1])
    # walls = int(input("What size of a maze do you want to make?"))
    # cell = int(input("What size of a maze do you want to make?"))
    start_time = time.time()

    # TODO add a option that asks if the user wants to save the maze.
    
    walls = 5
    cell = 10

    x, y = generate(sizex, sizey)
    run(x, y, cell, walls, sizex, sizey, f'{sizex}x{sizey}', save="show")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.6f} seconds")

