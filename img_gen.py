from PIL import Image
import numpy as np


def init(size_x, size_y, walls, cell, wall_color=[255, 255, 255], cell_color=[0, 0, 0]):
    """Sets the initial numpy array"""
    # TODO There is a probably a better way to scale these, look into it.
    pixels_y = (size_x * cell) + (walls * (size_x+1))
    pixels_x = (size_y * cell) + (walls * (size_y+1))
    print(f"Image resolution is {pixels_y}x{pixels_x}")
    
    # Creates array with each RGB Layer and then combines them into array a
    x = np.full((pixels_x, pixels_y), cell_color[0], dtype=np.uint8)
    y = np.full((pixels_x, pixels_y), cell_color[1], dtype=np.uint8)
    z = np.full((pixels_x, pixels_y), cell_color[2], dtype=np.uint8)
    a = np.stack((x, y, z), axis=-1, dtype=np.uint8)

    
    # Vertical walls
    for y in range(pixels_y):
        for x in range(pixels_x):
            if (x % (cell + walls)) < walls or (y % (cell + walls)) < walls:
                a[x][y] = wall_color
                 
    # Horizontal walls
    for x in range(pixels_x):
        for y in range(pixels_y):
            if (x % (cell + walls)) < walls or (y % (cell + walls)) < walls:
                a[x][y] = wall_color

    return a


# TODO Both of these functions split the positions accordingly, this can probably be condensed.
# Recolor also does something similar, maybe use args?
def horizon_wall(a, pos1, pos2, cellsize, wallsize, cell_color=[0, 0, 0]):
    pos1 = pos1.split(" ")
    pos2 = pos2.split(" ")
    y1 = int(pos1[1])
    y2 = int(pos2[1])
    # Doubling up here for no reason
    ypos = max([int(pos1[1]), int(pos2[1])])
    xpos = max([int(pos1[0]), int(pos2[0])])
    x_off = ((wallsize + cellsize) * ypos)
    y_off = ((wallsize + cellsize) * xpos) + wallsize
    for x in range(wallsize):
        for y in range(cellsize):
            a[x+x_off][y+y_off] = cell_color
 

def vertical_wall(a, pos1, pos2, cellsize, wallsize, cell_color=[0, 0, 0]):
    pos1 = pos1.split(" ")
    pos2 = pos2.split(" ")
    x1 = int(pos1[0])
    x2 = int(pos2[0])
    # Doubling up here for no reason
    ypos = max([int(pos1[1]), int(pos2[1])])
    xpos = max([int(pos1[0]), int(pos2[0])])
    y_off = (wallsize + cellsize) * xpos
    x_off = ((wallsize + cellsize) * ypos) + wallsize
    for y in range(wallsize):
        for x in range(cellsize):
            a[x+x_off][y+y_off] = cell_color


def recolor(a, position, cellsize, wallsize, color):
    position = position.split(" ")
    ypos = int(position[1])
    xpos = int(position[0])
    y_off = (wallsize + cellsize) * xpos + wallsize
    x_off = ((wallsize + cellsize) * ypos) + wallsize
    for x in range(cellsize):
        for y in range(cellsize):
            if a[x+x_off][y+y_off][0] == 255 or a[x+x_off][y+y_off][1] == 255: 
                pass
            else:
                a[x+x_off][y+y_off] = color


def move(a, pos1, pos2, cellsize, wallsize, neighbors_dict):
    # This is kinda messy, can be reformatted for sure
    pos1_mod = pos1.split(" ")
    pos2_mod = pos2.split(" ")
    x1 = int(pos1_mod[0])
    y1 = int(pos1_mod[1])
    x2 = int(pos2_mod[0])
    y2 = int(pos2_mod[1])
    x_vals = [x1, x2]
    y_vals = [y1, y2]
    if  max(x_vals) - min(x_vals) != 0:
        vertical_wall(a, pos1, pos2, cellsize, wallsize)
    if  max(y_vals) - min(y_vals) != 0:
        horizon_wall(a, pos1, pos2, cellsize, wallsize)


def run(test_path, test_neighbors, cell, walls, size_x, size_y, name=None, in_array='No', save=False, return_array=False):
    if name == None:
        name = str(size_x) + 'x' +  str(size_y)
    if isinstance(in_array, np.ndarray) != True:
        a = init(size_x, size_y, walls, cell)
    if isinstance(in_array, np.ndarray) == True:
        a = in_array
        print("Loaded Array")



    # Need to set starting position color
    # Colors the Maze Start Green
    # recolor(a, test_path[0], cell, walls, [0, 255, 0])
    for move_val in range(len(test_path)):
        if (move_val) == (len(test_path)-1):
            pass
        elif test_path[move_val-1] in test_neighbors[test_path[move_val]]:
            # Create Color
            # recolor(a, test_path[move_val], cell, walls, [50, 50, 50])
            # recolor(a, test_path[move_val-1], cell, walls, [100, 100, 100])
    
            move(a, test_path[move_val], test_path[move_val-1], cell, walls, test_neighbors)
            # This is for if you want to save an animation
            # im = Image.fromarray(a)
            # im = im.convert('RGB')
            # im.save(f"{move_val}.jpg")
    
            # Remove Color
            # recolor(a, test_path[move_val], cell, walls, [0, 0, 0])
            # recolor(a, test_path[move_val-1], cell, walls, [0, 0, 0])
    
        else:
            # If you have issues with weird looking mazes, the problem is here I think
            t = test_path[:move_val-1]
            t.reverse()
                
            for _ in t:
                if _ not in test_neighbors[test_path[move_val]]:
                    pass
                else:
                    # Create Color
                    # recolor(a, test_path[move_val], cell, walls, [0, 0, 0])
                    # recolor(a, _, cell, walls, [0, 0, 0]) 
    
                    move(a, test_path[move_val], _, cell, walls, test_neighbors)
                    # This is for if you want to save an animation
                    # im = Image.fromarray(a)
                    # im = im.convert('RGB')
                    # im.save(f"{move_val}.jpg")
    
                    # Remove Color
                    # recolor(a, test_path[move_val], cell, walls, [0, 0, 0])
                    # recolor(a, _, cell, walls, [0, 0, 0])
                    break
    # Accounts for the proper pixel size by adding extra pixel in the middle if needed

    # QUARANTINE
    # Adjust for maximum Y Value
    """
    adjustment = (max_y - a.shape[0]) // 2
    if adjustment > 0:
        # a = np.repeat(a, [1+adjustment, 1+adjustment], axis=0)
        first = a[0, :, :]
        first = first.reshape(1, 1280, 3)
        last = a[-1, :, :]
        last = last.reshape(1, 1280, 3)

        for _ in range(adjustment):
            a = np.concatenate((first, a, last), axis=0)
        print()
        print(f"a.shape is {a.shape}")
        print(f"max_y is {max_y}")


    adjustment = (max_y - a.shape[0]) % 2
    if adjustment > 0:
        loc = (a.shape[0]) // 2
        row = a[loc]
        a = np.insert(a, loc, row, axis=0)
        if a.shape[0] != max_y:
            print("ERROR WITH SHAPE")
            return
            """



    if save == True:
        im = Image.fromarray(a)
        im = im.convert('RGB')
        im.save(f"{name}.jpg")
    if save == 'show':
        im = Image.fromarray(a)
        im = im.convert('RGB')
        im.show()
    if return_array == True:
        return a


if __name__ == "__main__":
    # test_path = ['0 0', '0 1', '0 2', '1 2', '2 2', '2 3', '3 3', '3 4', '4 4', '4 3', '4 2', '4 1', '4 0', '3 0', '2 0', '3 1', '2 4', '1 4', '0 4', '3 2', '2 1', '1 3', '0 3', '1 1', '1 0']
    # test_neighbors = {'0 0': ['0 1', '1 0'], '0 1': ['0 2', '0 0', '1 1'], '0 2': ['0 1', '1 2', '0 3'], '0 3': ['0 2', '0 4', '1 3'], '0 4': ['1 4', '0 3'], '1 0': ['0 0', '2 0', '1 1'], '1 1': ['0 1', '1 2', '2 1', '1 0'], '1 2': ['0 2', '1 1', '2 2', '1 3'], '1 3': ['2 3', '1 4', '1 2', '0 3'], '1 4': ['0 4', '1 3', '2 4'], '2 0': ['3 0', '2 1', '1 0'], '2 1': ['2 0', '1 1', '2 2', '3 1'], '2 2': ['2 3', '3 2', '1 2', '2 1'], '2 3': ['2 2', '3 3', '1 3', '2 4'], '2 4': ['2 3', '1 4', '3 4'], '3 0': ['4 0', '2 0', '3 1'], '3 1': ['4 1', '3 0', '3 2', '2 1'], '3 2': ['2 2', '4 2', '3 3', '3 1'], '3 3': ['2 3', '3 4', '3 2', '4 3'], '3 4': ['4 4', '3 3', '2 4'], '4 0': ['4 1', '3 0'], '4 1': ['4 0', '4 2', '3 1'], '4 2': ['4 1', '3 2', '4 3'], '4 3': ['4 4', '4 2', '3 3'], '4 4': ['3 4', '4 3']}
    test_path = ['0 0', '0 1', '0 2', '0 3', '0 4', '1 4', '2 4', '2 3', '3 3', '4 3', '5 3', '6 3', '7 3', '7 4', '7 2', '7 1', '6 1', '6 0', '5 0', '4 0', '4 1', '3 1', '2 1', '2 0', '3 0', '5 1', '7 0', '6 4', '6 2', '5 2', '5 4', '4 2', '4 4', '3 2', '2 2', '3 4', '1 3', '1 2', '1 1', '1 0']
    test_neighbors = {'0 0': ['0 1', '1 0'], '0 1': ['0 2', '0 0', '1 1'], '0 2': ['0 1', '0 3', '1 2'], '0 3': ['0 4', '0 2', '1 3'], '0 4': ['0 3', '1 4'], '1 0': ['0 0', '2 0', '1 1'], '1 1': ['0 1', '2 1', '1 0', '1 2'], '1 2': ['2 2', '0 2', '1 3', '1 1'], '1 3': ['2 3', '0 3', '1 4', '1 2'], '1 4': ['2 4', '0 4', '1 3'], '2 0': ['3 0', '2 1', '1 0'], '2 1': ['3 1', '2 2', '2 0', '1 1'], '2 2': ['2 3', '2 1', '3 2', '1 2'], '2 3': ['3 3', '2 4', '2 2', '1 3'], '2 4': ['2 3', '3 4', '1 4'], '3 0': ['3 1', '4 0', '2 0'], '3 1': ['4 1', '3 0', '2 1', '3 2'], '3 2': ['3 3', '3 1', '4 2', '2 2'], '3 3': ['2 3', '3 4', '4 3', '3 2'], '3 4': ['3 3', '4 4', '2 4'], '4 0': ['5 0', '4 1', '3 0'], '4 1': ['3 1', '4 2', '4 0', '5 1'], '4 2': ['5 2', '4 1', '4 3', '3 2'], '4 3': ['3 3', '5 3', '4 2', '4 4'], '4 4': ['3 4', '5 4', '4 3'], '5 0': ['6 0', '4 0', '5 1'], '5 1': ['5 2', '5 0', '4 1', '6 1'], '5 2': ['5 3', '4 2', '5 1', '6 2'], '5 3': ['6 3', '5 2', '5 4', '4 3'], '5 4': ['5 3', '4 4', '6 4'], '6 0': ['5 0', '6 1', '7 0'], '6 1': ['6 0', '5 1', '7 1', '6 2'], '6 2': ['6 3', '5 2', '7 2', '6 1'], '6 3': ['5 3', '7 3', '6 4', '6 2'], '6 4': ['6 3', '7 4', '5 4'], '7 0': ['6 0', '7 1'], '7 1': ['7 2', '6 1', '7 0'], '7 2': ['7 3', '7 1', '6 2'], '7 3': ['6 3', '7 4', '7 2'], '7 4': ['7 3', '6 4']}
    init_size_x = 8
    init_size_y = 5
    init_walls = 5
    init_cell = 50

    run(test_path, test_neighbors, init_cell, init_walls, init_size_x, init_size_y, save='show')
        
