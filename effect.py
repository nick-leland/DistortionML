import numpy as np
from PIL import Image
from scipy.interpolate import griddata

def polar_transform(x, y, warp_point_x, warp_point_y, a=2, b=2.5):
    dx, dy = x - warp_point_x, y - warp_point_y
    r = np.sqrt(dx**2 + dy**2)
    theta = np.arctan2(dy, dx)
    rn = (r / a)**(1/b)
    return rn, theta

def cartesian(r, theta, warp_point_x, warp_point_y):
    x = warp_point_x + r * np.cos(theta)
    y = warp_point_y + r * np.sin(theta)
    return x, y

if __name__ == "__main__":
    posx, posy = 0.5, 0.5
    I = np.asarray(Image.open('15x15_1_10g.jpg'))
    ya, xa = I.shape[:2]
    centerx = xa * posx
    centery = ya * posy
    print(centerx, centery)
    print(f"I Shape is {I.shape}")

    max_factor = 1
    factor = 0
    while factor < max_factor:
        print(f"Factor is {round(factor, 3)}")
        factor += 0.001
        
        y, x = np.mgrid[0:ya, 0:xa]
        r, theta = polar_transform(x, y, centerx, centery, a=2*factor, b=2.5*factor)
        src_x, src_y = cartesian(r, theta, centerx, centery)
        
        distort = np.zeros_like(I)
        
        for c in range(I.shape[2]):  # Apply to each color channel
            distort[:,:,c] = griddata((x.flatten(), y.flatten()), I[:,:,c].flatten(), 
                                      (src_x, src_y), method='cubic', fill_value=0)
        
        distort = distort.astype(np.uint8)
        distort_output = Image.fromarray(distort)
        distort_output.save(f"effect_output/{round(factor*1000)}.jpg")

        print(f"Processed image for factor {round(factor, 3)}")
