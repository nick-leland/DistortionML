import numpy as np
from scipy import ndimage

def apply_vector_field_transform(image, func, radius=100, center=None, strength=1):
    """
    Apply a vector field transformation to an image based on a given multivariate function.
    
    :param image: Input image as a numpy array (height, width, channels)
    :param func: A function that takes x and y as inputs and returns a scalar
    :param radius: Radius of the effect
    :param center: Tuple (y, x) for the center of the effect. If None, use the image center.
    :param strength: Strength of the effect
    :return: Transformed image as a numpy array
    """
    rows, cols = image.shape[:2]
    
    if center is None:
        center = (rows // 2, cols // 2)
    
    y, x = np.ogrid[:rows, :cols]
    y = y - center[0]
    x = x - center[1]
    
    # Calculate distance from center
    dist_from_center = np.sqrt(x**2 + y**2)
    
    # Normalize coordinates
    x_norm = x / radius
    y_norm = y / radius
    
    # Calculate function values
    z = func(x_norm, y_norm)
    
    # Calculate gradients
    gy, gx = np.gradient(z)
    
    # Apply circular limit
    mask = dist_from_center <= radius
    gx = gx * mask
    gy = gy * mask
    
    # Normalize gradient vectors
    magnitude = np.sqrt(gx**2 + gy**2)
    magnitude[magnitude == 0] = 1  # Avoid division by zero
    gx = gx / magnitude
    gy = gy / magnitude
    
    # Scale the effect
    gx = gx * strength * (dist_from_center / radius)
    gy = gy * strength * (dist_from_center / radius)
    
    # Create the mapping
    x_new = x + gx
    y_new = y + gy
    
    # Ensure the new coordinates are within the image boundaries
    x_new = np.clip(x_new + center[1], 0, cols - 1)
    y_new = np.clip(y_new + center[0], 0, rows - 1)
    
    # Apply the transformation to each channel
    channels = [ndimage.map_coordinates(image[..., i], [y_new, x_new], order=1, mode='reflect') 
                for i in range(image.shape[2])]
    
    return np.dstack(channels).astype(image.dtype)

# Example usage:
# import matplotlib.pyplot as plt
# from PIL import Image

# # Load an image
# image = np.array(Image.open('path_to_your_image.jpg'))

# # Define a multivariate function (e.g., for a bulge effect)
# def bulge_function(x, y):
#     return x**2 + y**2

# # Apply the transformation
# transformed_image = apply_vector_field_transform(image, bulge_function, radius=100, strength=5)

# # Display the result
# plt.imshow(transformed_image)
# plt.axis('off')
# plt.show()
