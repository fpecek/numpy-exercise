import numpy as np
import matplotlib.pyplot as plt
from scipy import misc


# Define a main() function that manipulate and show the picture.
def main():
    face = misc.face(gray=True)  # create 2D image array. If set gray to False, it will be 3D array

    # display image in gray colormap
    plt.imshow(face, cmap='gray')
    plt.show()

    # crop image and display it
    crop_img = face[50:-200, 200:-100]
    plt.imshow(crop_img, cmap='gray')
    plt.show()

    # frame raccoon face in ellipse
    sy, sx = face.shape  # (768, 1024)
    y, x = np.ogrid[0:sy, 0:sx]  # x and y indices of pixels

    center_x, center_y = (660, 300)  # center of the raccoon face

    # mask = ((x - center_x)**2 + (y - center_y)**2) > 230**2 # circle
    mask_ellipse = ((x - center_x) ** 2 / 2 + (y - center_y) ** 2) > 230 ** 2  # ellipse

    face[mask_ellipse] = 0

    plt.imshow(face)
    plt.show()


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
