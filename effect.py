import numpy as np
from PIL import Image

# The goal of this effect is to create an image bulge
# Using the stack overflow algorithm :
# https://math.stackexchange.com/questions/266250/explanation-of-this-image-warping-bulge-filter-algorithm

"""
.5 is representative of the center of the picture for a central warp.  

First we need to convert our pixels to polar form
r = Sqrt[(x - .5)^2 + (y - .5)^2]
(Also representative as tan^-1)
a = ArcTan[x - .5, y - .5]

This gives us (r, a)

We take this polar point and then map it to a new location:
(rn, a)

rn = (r^2.5)/.5

Where does this 2.5/.5 come from?
This is really what creates the bulging effect


ArcTan is not really necessary since Cos[a] = (x - .5) / r 
                                 and Sin[a] = (y - .5) / r

Then, remap your pixels according to:
x -> rn*Cos[a] + .5
y -> rn*Sin[a] + .5
"""

# Actual code begins here:

def polar(x, y, warp_point_x, warp_point_y, a=2, b=2.5):
    r = ((( x - warp_point_x) ** 2) + ((y - warp_point_y) ** 2))
    a = np.arctan([(x - warp_point_x), (y - warp_point_y)])
    rn = ( a * r ) ** b
    return rn, a

if __name__ == "__main__":
    posx, posy = 0.5, 0.5
    I = np.asarray(Image.open('15x15_1_10g.jpg'))
    distort = np.empty(I.shape)
    x = I.shape[0]
    I = I.reshape([I.shape[0]**2, 3])
    counter = 0
    print(I.shape[0])
    print(distort.shape[0])
    x, y = 0, 0
    # for num in range(I.shape[0]):
    for num in range(16):
        print(num)
        # This is 0 index
        print(x, y)
        x += 1
        if (num // distort.shape[0] == 0):
            print("jumping")
            y += 1
            x = 0


