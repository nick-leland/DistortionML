import numpy as np

# The goal of this effect is to create an image bulge
# Using the stack overflow algorithm :
# https://math.stackexchange.com/questions/266250/explanation-of-this-image-warping-bulge-filter-algorithm

r = ((x - 0.5) ** 2 + (y - 0.5) ** 2) ** (1/2)
a = np.arctan(
