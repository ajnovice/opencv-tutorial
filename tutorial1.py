import numpy as np
from cv2 import cv2 as cv


def read_image(read_mode=1, image_path=None):
    img = cv.imread(image_path, read_mode)
    return img


def show_image(image_name, image):
    cv.imshow(image_name, image)
    cv.waitKey(100)
    cv.destroyAllWindows()


img = read_image(0, "dp.jpeg")
show_image("image", img)