import numpy as np
from PIL import Image
import os
import sys
from os import path

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0, parent_dir)
import transformation
from transformation import apply_vector_field_transform

from dfs_generation import generate
from bulk_bulge_generation import definitions
from img_gen import init, run
import sys


def yolo_output(obj_id, x, y, w, h, all_ids):
    if len(str(obj_id)) > len(str(max(all_ids))):
         spaces = " " * len(str(max(all_ids))) - len(str(obj_id))
    else:
         spaces = ''
    
    return f"{obj_id}{spaces} {x} {y} {w} {h}"


if __name__ == "__main__":
    print("This program is used to generate mazes, bulges (of previously generated mazes) and fresh mazes for training use.")
    x = input("If you would like to continue plese type [y]es or [n]o\n")
    print(x)
    if x == "n" or x == "no":
        sys.exit()
    else:
        # Creates the generator
        rng = np.random.default_rng()

        # Sets the split of data
        train, val, test = 0.8, 0.1, 0.1
        # Whether or not they are filled
        train_status, val_status, test_status = False, False, False

        # We want to create one dataset where we use mazes and bulge the same mazes, and one where we use different mazes.

        # Sets our main directory
        os.makedirs("data", exist_ok=True)
        os.chdir("data/")
        
        os.makedirs("test", exist_ok=True)
        os.chdir("test/")
        os.makedirs("images", exist_ok=True)
        os.makedirs("labels", exist_ok=True)
        os.chdir("../")

        os.makedirs("train", exist_ok=True)
        os.chdir("train")
        os.makedirs("images", exist_ok=True)
        os.makedirs("labels", exist_ok=True)
        os.chdir("../")

        os.makedirs("valid", exist_ok=True)
        os.chdir("valid")
        os.makedirs("images", exist_ok=True)
        os.makedirs("labels", exist_ok=True)
        os.chdir("../")

        # Base parameters
        size_x = 25
        size_y = 25
        walls = 3
        cell = 15
        x = int(input("How many pictures would you like to generate?"))

        train_run = round(train * x)
        val_run = round(val * x)
        test_run = round(test * x)


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

        counter_train, counter_test, counter_val = 0, 0, 0
        print(train_run)
        print(test_run)
        print(val_run)

        for _ in range(sum([train_run, val_run, test_run])):
            # Sets the initial file selection
            print()
            print(counter_train, counter_test, counter_val)
            print()
            if counter_train != train_run:
                counter_train += 1
                os.chdir("train/images")
            elif counter_test != test_run:
                counter_test += 1
                print("Time for test images")
                os.chdir("test/images")
            elif counter_val != val_run:
                counter_val += 1
                print("Time for validation images")
                os.chdir("valid/images")




            print(f"{_}/{x}")
            # Generates grids for the initial maze creation
            # b = init(size_x, size_y, walls, cell)

            # path_fresh, neighbors_fresh = generate(size_x, size_y)

            # # Creates and saves a fresh maze
            # fresh_maze = run(path_fresh, neighbors_fresh, cell, walls, size_x, size_y, name=f"{_}_fresh", in_array=b, save=True, return_array=True)
            # Currently disabled, only generating initial maze

            # os.chdir("../maze/")

            # Generate maze from grid
            path, neighbors = generate(size_x, size_y)
            a = init(size_x, size_y, walls, cell)
            maze = run(path, neighbors, cell, walls, size_x, size_y, name=f"{_}_maze", in_array=a, save=True, return_array=True)

            # os.chdir("../distorted/")

            radius, location, strength, edge_smoothness= definitions(rng)
            center_x = location[0]
            center_y = location[1]
            print("Location (x, y)")
            print(f"({center_x}, {center_y})")

            # Using a 0 smooth in order to add harsh values
            edge_smoothness = 0
            center_smoothness = 0

            transformed , (gx, gy) = apply_vector_field_transform(maze, bulge, radius, (center_x, center_y), strength, edge_smoothness, center_smoothness)

            transformed_out = Image.fromarray(transformed)
            transformed_output = transformed_out.convert('RGB')
            transformed_out.save(f"{_}_distorted.jpg")

            

            size = radius * 2
            yolo = yolo_output(label, center_x, (1-center_y), size, size, ids)
            # os.chdir("../../labels/distorted")
            os.chdir("../labels")

            f = open(f"{_}_distorted.txt", "wt")
            f.write(yolo)
            f.close()

            result = Image.fromarray(transformed)
            os.chdir("../../")

            # if counter_train != train_run:
            #     counter_train += 1
            # if counter_test != test_run:
            #     counter_test += 1
            # if counter_val != val_run:
            #     counter_val += 1


