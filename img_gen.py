from PIL import Image
import numpy as np

rng = np.random.default_rng()
pixels= 248

# Currently just making random pixels to verify image generation
a = rng.integers(2, size=(pixels, pixels))

print(a)

im = Image.frombytes("1", (pixels, pixels), a.tobytes())

print(im.format, im.size, im.mode)
# im.show()

