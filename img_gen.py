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

        
im = Image.fromarray(a * 255)
im = im.convert('L')

print(im.format, im.size, im.mode)
im.show()
# im.save("test.jpg")
