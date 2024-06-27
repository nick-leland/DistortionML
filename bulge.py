import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import scipy

def gradient_f(x, y):
    # return 2*x, 2*y
    return 2*x, 2*y

def create_displacement_map(width, height, scale=1.0):
    x = np.linspace(-1, 1, width)
    y = np.linspace(-1, 1, height)
    X, Y = np.meshgrid(x, y)
    
    U, V = gradient_f(X, Y)
    
    # Normalize the vectors
    magnitude = np.sqrt(U**2 + V**2)
    max_magnitude = np.max(magnitude)
    if max_magnitude != 0:
        U = U / magnitude.max() * scale * (width / 2)
        V = V / magnitude.max() * scale * (height / 2)
    
    return U, V

def transform_image(image_path, output_path, scale=0.5):
    # Load the image
    img = Image.open(image_path)
    width, height = img.size
    
    # Create displacement map
    U, V = create_displacement_map(width, height, scale)
    
    # Create a grid of coordinates
    x = np.arange(width)
    y = np.arange(height)
    X, Y = np.meshgrid(x, y)
    
    # Apply displacement
    X_prime = (X + U).astype(np.float32)
    Y_prime = (Y + V).astype(np.float32)
    
    # Ensure the new coordinates are within the image bounds
    X_prime = np.clip(X_prime, 0, width - 1)
    Y_prime = np.clip(Y_prime, 0, height - 1)
    
    # Remap pixels
    pixels = np.array(img)
    new_pixels = np.zeros_like(pixels)
    for i in range(3):  # for each color channel
        new_pixels[:,:,i] = scipy.ndimage.map_coordinates(pixels[:,:,i], [Y_prime, X_prime], order=1)
    
    # Create and save the new image
    new_img = Image.fromarray(new_pixels.astype('uint8'))
    new_img.save(output_path)
    print(f"Transformed image saved as '{output_path}'")

# Usage
transform_image('15x15_3_15g.jpg', 'output_image.jpg', scale=0.5)
