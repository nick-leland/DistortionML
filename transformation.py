import numpy as np
from PIL import Image
from scipy import ndimage
import matplotlib.pyplot as plt

def apply_vector_field_transform(image, func, radius, center=(0.5, 0.5), strength=1, edge_smoothness=0.1, center_smoothness=0.20):
    # 0.106 strength = .50
    # 0.106 strength = 1
    rows, cols = image.shape[:2]
    max_dim = max(rows, cols)
    
    #Normalize the positions
    # Y Needs to be flipped
    center_y = int(center[1] * rows)
    center_x = int(center[0] * cols)

    # Inverts the Y axis (Numpy is 0 index at top of image)
    center_y = abs(rows - center_y)

    print()
    print(rows, cols)
    print("y =", center_y, "/", rows)
    print("x =", center_x, "/", cols)
    print()
    
    pixel_radius = int(max_dim * radius)
    
    y, x = np.ogrid[:rows, :cols]
    y = (y - center_y) / max_dim
    x = (x - center_x) / max_dim
    
    # Calculate distance from center
    dist_from_center = np.sqrt(x**2 + y**2)
    
    # Calculate function values
    z = func(x, y)
    
    # Calculate gradients
    gy, gx = np.gradient(z)

    # Creating a sigmoid function to apply to masks
    def sigmoid(x, center, steepness):
        return 1 / (1 + np.exp(-steepness * (x - center)))
    
    print(radius)
    print(strength)
    print(edge_smoothness)
    print(center_smoothness)

    # Masking
    edge_mask = np.clip((radius - dist_from_center) / (radius * edge_smoothness), 0, 1)

    center_mask = np.clip((dist_from_center - radius * center_smoothness) / (radius * center_smoothness), 0, 1)

    mask = edge_mask * center_mask
    
    # Apply mask to gradients
    gx = gx * mask
    gy = gy * mask
    
    # Normalize gradient vectors
    magnitude = np.sqrt(gx**2 + gy**2)
    magnitude[magnitude == 0] = 1  # Avoid division by zero
    gx = gx / magnitude
    gy = gy / magnitude
    
    # Scale the effect (Play with the number 5)
    scale_factor = strength * np.log(max_dim) / 100  # Adjust strength based on image size
    gx = gx * scale_factor * mask
    gy = gy * scale_factor * mask
    
    # Create the mapping
    x_new = x + gx
    y_new = y + gy
    
    # Convert back to pixel coordinates
    x_new = x_new * max_dim + center_x
    y_new = y_new * max_dim + center_y
    
    # Ensure the new coordinates are within the image boundaries
    x_new = np.clip(x_new, 0, cols - 1)
    y_new = np.clip(y_new, 0, rows - 1)
    
    # Apply the transformation to each channel
    channels = [ndimage.map_coordinates(image[..., i], [y_new, x_new], order=1, mode='reflect') 
                for i in range(image.shape[2])]
    
    transformed_image = np.dstack(channels).astype(image.dtype)
    
    return transformed_image, (gx, gy)


def create_gradient_vector_field(gx, gy, image_shape, step=20, reverse=False):
    """
    Create a gradient vector field visualization with option to reverse direction.
    
    :param gx: X-component of the gradient
    :param gy: Y-component of the gradient
    :param image_shape: Shape of the original image (height, width)
    :param step: Spacing between arrows
    :param reverse: If True, reverse the direction of the arrows
    :return: Gradient vector field as a numpy array (RGB image)
    """
    rows, cols = image_shape
    y, x = np.mgrid[step/2:rows:step, step/2:cols:step].reshape(2, -1).astype(int)
    
    # Calculate the scale based on image size
    max_dim = max(rows, cols)
    scale = max_dim / 1000  # Adjusted for longer arrows
    
    # Reverse direction if specified
    direction = -1 if reverse else 1
    
    fig, ax = plt.subplots(figsize=(cols/50, rows/50), dpi=100)
    ax.quiver(x, y, direction * gx[y, x], direction * -gy[y, x], 
              scale=scale, 
              scale_units='width', 
              width=0.002 * max_dim / 500,
              headwidth=8, 
              headlength=12, 
              headaxislength=0, 
              color='black',
              minshaft=2,
              minlength=0,
              pivot='tail')
    ax.set_xlim(0, cols)
    ax.set_ylim(rows, 0)
    ax.set_aspect('equal')
    ax.axis('off')
    
    fig.tight_layout(pad=0)
    fig.canvas.draw()
    vector_field = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
    vector_field = vector_field.reshape(fig.canvas.get_width_height()[::-1] + (3,))
    plt.close(fig)
    
    return vector_field

def transform_image(image, func_choice, radius, center_x, center_y, strength, edge_smoothness, reverse_gradient=True, spiral_frequency=1):
    I = np.asarray(Image.open(image))    

    def pinch(x, y):
        return x**2 + y**2

    def shift(x, y):
        return np.arctan2(y, x)

    def bulge(x, y):
        r = np.sqrt(x**2 + y**2)
        # return -1 / (r + 1)
        return -r 

    def spiral(x, y, frequency=1):
        r = np.sqrt(x**2 + y**2)
        theta = np.arctan2(y, x)
        return r * np.sin(theta - frequency * r)

    if func_choice == "Pinch":
        func = pinch
    elif func_choice == "Spiral":
        func = shift 
    elif func_choice == "Bulge":
        func = bulge
    elif func_choice == "Shift":
        func = lambda x, y: spiral(x, y, frequency=spiral_frequency)

    transformed, (gx, gy) = apply_vector_field_transform(I, func, radius, (center_y, center_x), strength, edge_smoothness)
    vector_field = create_gradient_vector_field(gx, gy, I.shape[:2], reverse=reverse_gradient)

    return transformed, vector_field

