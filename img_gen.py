from PIL import Image
import numpy as np

# Generic test values from generation algo
test_path = ['0 0', '0 1', '0 2', '1 2', '2 2', '2 3', '3 3', '3 4', '4 4', '4 3', '4 2', '4 1', '4 0', '3 0', '2 0', '3 1', '2 4', '1 4', '0 4', '3 2', '2 1', '1 3', '0 3', '1 1', '1 0']
test_neighbors = {'0 0': ['0 1', '1 0'], '0 1': ['0 2', '0 0', '1 1'], '0 2': ['0 1', '1 2', '0 3'], '0 3': ['0 2', '0 4', '1 3'], '0 4': ['1 4', '0 3'], '1 0': ['0 0', '2 0', '1 1'], '1 1': ['0 1', '1 2', '2 1', '1 0'], '1 2': ['0 2', '1 1', '2 2', '1 3'], '1 3': ['2 3', '1 4', '1 2', '0 3'], '1 4': ['0 4', '1 3', '2 4'], '2 0': ['3 0', '2 1', '1 0'], '2 1': ['2 0', '1 1', '2 2', '3 1'], '2 2': ['2 3', '3 2', '1 2', '2 1'], '2 3': ['2 2', '3 3', '1 3', '2 4'], '2 4': ['2 3', '1 4', '3 4'], '3 0': ['4 0', '2 0', '3 1'], '3 1': ['4 1', '3 0', '3 2', '2 1'], '3 2': ['2 2', '4 2', '3 3', '3 1'], '3 3': ['2 3', '3 4', '3 2', '4 3'], '3 4': ['4 4', '3 3', '2 4'], '4 0': ['4 1', '3 0'], '4 1': ['4 0', '4 2', '3 1'], '4 2': ['4 1', '3 2', '4 3'], '4 3': ['4 4', '4 2', '3 3'], '4 4': ['3 4', '4 3']}
size = 5


# Set the pixel side of the walls
# TODO There is a probably a better way to scale these, look into it.
walls = 5
cell = 50

pixels = (size * cell) + (walls * (size+1))
print(f"pixels are {pixels}")

# First lets try to make a grid
# a = np.empty((pixels, pixels), dtype=np.uint8)
a = np.zeros((pixels, pixels), dtype=np.uint8)

# Vertical
for x in range(pixels):
    for y in range(pixels):
        if (x % (cell + walls)) < walls or (y % (cell + walls)) < walls:
            # a[x][y] = 1  # Wall
            a[x][y] = 255  # Wall
             
# Horizontal
for y in range(pixels):
    for x in range(pixels):
        if (x % (cell + walls)) < walls or (y % (cell + walls)) < walls:
            # a[x][y] = 1  # Wall
            a[x][y] = 255  # Wall

# Now we will begin to follow the generate instruction to create the maze
# first = test_path[:2]
# print("First Move:")
# print(first)
# print("Corresponding Dictionary:")
# [print(f"'{x}' :", test_neighbors[x]) for x in first]

def horizon_wall(a, pos1, pos2, cellsize, wallsize):
    pos1 = pos1.split(" ")
    pos2 = pos2.split(" ")
    y1 = int(pos1[1])
    y2 = int(pos2[1])
    # Doubling up here for no reason
    ypos = max([int(pos1[1]), int(pos2[1])])
    xpos = max([int(pos1[0]), int(pos2[0])])
    # x_off = (wallsize + cellsize) * xpos
    x_off = ((wallsize + cellsize) * ypos)
    # y_off = wallsize
    y_off = ((wallsize + cellsize) * xpos) + wallsize
    for x in range(wallsize):
        for y in range(cellsize):
            a[x+x_off][y+y_off] = 0   


def vertical_wall(a, pos1, pos2, cellsize, wallsize):
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
            a[x+x_off][y+y_off] = 0   


def recolor(a, position, cellsize, wallsize, color):
    position = position.split(" ")
    ypos = int(position[1])
    xpos = int(position[0])
    y_off = (wallsize + cellsize) * xpos + wallsize
    x_off = ((wallsize + cellsize) * ypos) + wallsize
    for x in range(cellsize):
        for y in range(cellsize):
            # if a[x+x_off][y+y_off] == 100:
            #     a[x+x_off][y+y_off] = 0
            # elif a[x+x_off][y+y_off] == 0:
            #     a[x+x_off][y+y_off] = 100
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
    print("Position 1 =", x_vals)
    print("Position 2 =", y_vals)
    if  max(x_vals) - min(x_vals) != 0:
        print("X move, vertical wall removal")
        vertical_wall(a, pos1, pos2, cellsize, wallsize)
    if  max(y_vals) - min(y_vals) != 0:
        print("Y move, horizontal wall removal")
        horizon_wall(a, pos1, pos2, cellsize, wallsize)


print(test_path)
print("Length limit is", (len(test_path)-1))
for move_val in range(len(test_path)):
    if (move_val+1) > (len(test_path)-1):
        pass
    elif test_path[move_val+1] in test_neighbors[test_path[move_val]]:
        # Create Color
        recolor(a, test_path[move_val], cell, walls, 50)
        recolor(a, test_path[move_val+1], cell, walls, 100)
        move(a, test_path[move_val], test_path[move_val+1], cell, walls, test_neighbors)
        # This is for if you want to save an animation
        im = Image.fromarray(a)
        im = im.convert('L')
        im.save(f"{move_val}\t{test_path[move_val]}-{test_path[move_val+1]}.jpg")
        # Remove Color
        recolor(a, test_path[move_val], cell, walls, 0)
        recolor(a, test_path[move_val+1], cell, walls, 0)

    else:
        print(f"{test_path[move_val+1]} is not in {test_neighbors[test_path[move_val]]}")
        
# im = Image.fromarray(a * 255)
im = Image.fromarray(a)
im = im.convert('L')
im.show()
