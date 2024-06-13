import numpy as np
from PIL import Image
from img_gen import run
from gen import generate

if __name__ == "__main__":
    size = int(input("What size of a maze do you want to make?"))
    # walls = int(input("What size of a maze do you want to make?"))
    # cell = int(input("What size of a maze do you want to make?"))

    walls = 5
    cell = 10

    x, y = generate(size)
    run(x, y, cell, walls, size, size)

