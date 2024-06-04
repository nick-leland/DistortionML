import numpy as np

size = 10

x = np.zeros((size, size), dtype=np.int16)
print(x)

# Current Maze
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # #

# TODO Look more into the different types of rng within numpy
rng = np.random.default_rng()

directions = rng.integers(low=1, high=4, size=(size**2)).reshape(size, size)

# This creates the associated directions for our maze
# TODO Possible improvement to 8 cardinal directions rather then 4
maze =  x + directions

# North is 1
# East is 2
# South is 3
# West is 4

def passage(x, y, grid):

    return





