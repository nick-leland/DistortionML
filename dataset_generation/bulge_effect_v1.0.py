import numpy as np
from PIL import Image

# This was one of my first attempts at writing this but caused too much ghosting on the final image converting to polar and back

def polar_transform(x, y, warp_point_x, warp_point_y, a=2, b=2.5):
    r = np.sqrt(((x - warp_point_x) ** 2) + ((y - warp_point_y) ** 2))
    theta = np.arctan2(y - warp_point_y, x - warp_point_x)
    # Be sure that this translates correclty to the distort_generation function
    rn = (a * r) ** b
    return rn, theta 


def cartesian(r, theta, warp_point_x, warp_point_y):
    x = r * np.cos(theta) + warp_point_x
    y = r * np.sin(theta) + warp_point_y
    return x, y


def distort_generation(I, factora, factorb, posx=0.5, posy=0.5):
    distort = np.zeros_like(I)

    ya, xa = I.shape[:2]
    finalx = xa * posx
    finaly = ya * posy

    for x in range(xa):
        for y in range(ya):
            r, theta = polar_transform(x, y, finalx, finaly, a=2*factora, b=2.5*factorb)
            xn, yn = cartesian(r, theta, finalx, finaly)
                    
            # Bilinear interpolation
            x0, y0 = int(xn), int(yn)
            x1, y1 = min(x0 + 1, xa - 1), min(y0 + 1, ya - 1)
            dx, dy = xn - x0, yn - y0

            for c in range(3):  # For each color channel
                try:
                    distort[y, x, c] = (1 - dx) * (1 - dy) * I[y0, x0, c] + \
                                        dx * (1 - dy) * I[y0, x1, c] + \
                                        (1 - dx) * dy * I[y1, x0, c] + \
                                        dx * dy * I[y1, x1, c]
                except IndexError:
                    pass

    distort = np.clip(distort, 0, 255).astype(np.uint8)
    return distort


def main(image, factor=1, generate=False, posx=0.5, posy=0.5, save=False, show=False, factora=0, factorb=0):
    # posx, posy = 0.5, 0.5
    I = np.asarray(Image.open(image))
    print(f"I Shape is {I.shape}")

    if generate == True:
        max_factor = 1
        while (factora < max_factor) or (factorb < max_factor):
            print(f"Factor is {round(factor, 3)}")
            factora += 0.001
            factorb += 0.001

            # FactorA and FactorB should be a ratio related to the overall image size
            distort = distort_generation(I, factora, factorb)
            distort_output = Image.fromarray(distort)
            if save == True:
                distort_output.save(f"effect_output/{round(factor*1000)}.jpg")
            if show == True:
                distort_output.show()
            

            print(f"Processed image for factor {round(factor, 3)}")
        print("Completed generation") 

    else:
        distort = distort_generation(I, factora, factorb, posx, posy)
        distort_output = Image.fromarray(distort)
        if save == True:
            distort_output.save(f"effect_output/output.jpg")
        if show == True:
            distort_output.show()


if __name__ == "__main__":
    print("This script can also be used to generate images in bulk.  Please edit main function for more information")
    print("Note, this is outdated and isn't up entirely functioning.")
    image = input("Please give the file path to the image that will be distorted\n")
    factor=0.01 * int(input("Please give a factor number (0-100)\n"))
    main(image, generate=False, show=True, factora=factor, factorb=factor)

