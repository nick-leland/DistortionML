from PIL import Image
import numpy as np

# Generic test values from generation algo
test_path = ['0 0', '0 1', '0 2', '1 2', '2 2', '2 3', '3 3', '3 4', '4 4', '4 3', '4 2', '4 1', '4 0', '3 0', '2 0', '3 1', '2 4', '1 4', '0 4', '3 2', '2 1', '1 3', '0 3', '1 1', '1 0']
test_neighbors = {'0 0': ['0 1', '1 0'], '0 1': ['0 2', '0 0', '1 1'], '0 2': ['0 1', '1 2', '0 3'], '0 3': ['0 2', '0 4', '1 3'], '0 4': ['1 4', '0 3'], '1 0': ['0 0', '2 0', '1 1'], '1 1': ['0 1', '1 2', '2 1', '1 0'], '1 2': ['0 2', '1 1', '2 2', '1 3'], '1 3': ['2 3', '1 4', '1 2', '0 3'], '1 4': ['0 4', '1 3', '2 4'], '2 0': ['3 0', '2 1', '1 0'], '2 1': ['2 0', '1 1', '2 2', '3 1'], '2 2': ['2 3', '3 2', '1 2', '2 1'], '2 3': ['2 2', '3 3', '1 3', '2 4'], '2 4': ['2 3', '1 4', '3 4'], '3 0': ['4 0', '2 0', '3 1'], '3 1': ['4 1', '3 0', '3 2', '2 1'], '3 2': ['2 2', '4 2', '3 3', '3 1'], '3 3': ['2 3', '3 4', '3 2', '4 3'], '3 4': ['4 4', '3 3', '2 4'], '4 0': ['4 1', '3 0'], '4 1': ['4 0', '4 2', '3 1'], '4 2': ['4 1', '3 2', '4 3'], '4 3': ['4 4', '4 2', '3 3'], '4 4': ['3 4', '4 3']}
size = 10


# Set the pixel side of the walls
# TODO There is a probably a better way to scale these, look into it.
walls = 5
cell = 50

pixels = (size * cell) + (walls * (size+1))
print(pixels)

# First lets try to make a grid
a = np.empty((pixels, pixels), dtype=np.uint8)


# Vertical
for x in range(pixels):
    for y in range(pixels):
        if (x % (cell + walls)) < walls or (y % (cell + walls)) < walls:
            a[x][y] = 1  # Wall
             
# Horizontal
for y in range(pixels):
    for x in range(pixels):
        if (x % (cell + walls)) < walls or (y % (cell + walls)) < walls:
            a[x][y] = 1  # Wall

# Now we will begin to follow the generate instruction to create the maze
first = test_path[:2]
print("First Move:")
print(first)
print("Corresponding Dictionary:")
[print(f"'{x}' :", test_neighbors[x]) for x in first]

def eval_move(pos1, pos2):
    pos1 = pos1.split(" ")
    pos2 = pos2.split(" ")
    x1 = int(pos1[0])
    y1 = int(pos1[1])
    x2 = int(pos2[0])
    y2 = int(pos2[1])
    x_vals = [x1, x2]
    y_vals = [y1, y2]
    print("Position 1 =", x_vals)
    print("Position 2 =", y_vals)

    # This needs to be a relative position
    if  max(x_vals) - min(x_vals) != 0:
        print("X move, vertical wall removal")
    if  max(y_vals) - min(y_vals) != 0:
        print("Y move, horizontal wall removal")

# [0, 0] will always be in the top left location
# To find the walls, we need to move to the location in which the wall starts, and then loop for the duration
# 



print() 
eval_move(first[0], first[1])
print()

def horizon_wall(pos1, pos2, cellsize, wallsize):
    """Used to remove the wall between two horizontal positions"""
    print(pos1)
    print(pos2)

horizon_wall(first[0], first[1], cell, walls)

        
im = Image.fromarray(a * 255)
im = im.convert('L')

# print(im.format, im.size, im.mode)
# im.show()
# im.save("test.jpg")
