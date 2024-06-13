import numpy as np
from PIL import Image
from img_gen import run
from gen import generate
import time

if __name__ == "__main__":
    size = int(input("What size of a maze do you want to make?"))
    # walls = int(input("What size of a maze do you want to make?"))
    # cell = int(input("What size of a maze do you want to make?"))
    start_time = time.time()

    
    walls = 5
    cell = 10

    x, y = generate(size)
    run(x, y, cell, walls, size, size)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.6f} seconds")

