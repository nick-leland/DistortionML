import numpy as np
from PIL import Image
# from dataset_generation.img_gen import img_gen
from img_gen import init
# from dataset_generation.dfs_generation import dfs_generation
from dfs_generation import generate
import time

if __name__ == "__main__":
    size = input("What size of a grid do you want? Required format is '#x#'\n")
    if size == "":
        sizex = 5
        sizey = 4

    else:
        size = size.split("x") 
        sizex = int(size[0])
        sizey = int(size[1])

    walls = input("How many pixels wide are the walls?\n")
    if walls == "":
        walls = 5
        cell = 10
    else:
        walls = int(walls)
        cell = int(input("How many pixels wide are the cells?\n"))

    colors = input("What color are the walls? In the format 'xxx xxx xxx' with a max number of 255\nExample : '123 111 28\n")
    if colors == "":
        user_wall_color = [255, 255, 255]
        user_cell_color = [0, 0, 0]
    else:
        colors = colors.split(" ")
        user_wall_color = [int(colors[0]), int(colors[1]), int(colors[2])]

        colors = input("What color are the cell? In the format 'xxx xxx xxx' with a max number of 255\nExample : '123 111 28\n")
        colors = colors.split(" ")
        user_cell_color = [int(colors[0]), int(colors[1]), int(colors[2])]


    a = init(sizex, sizey, walls, cell, wall_color=user_wall_color, cell_color=user_cell_color)
    grid = Image.fromarray(a)
    grid = grid.convert('RGB')
    save = input("Do you want to save the image? Y/N?")
    if save.title() == 'Y':
        grid.save(f"{sizex}x{sizey}_{walls}_{cell}g.jpg")
        grid.show()

    if save.title() == 'N':
        grid.show()


