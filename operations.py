import cv2
import numpy as np
def opening(img):
    # define the kernel
    kernel = np.ones((3, 3), np.uint8)
    # opening the image
    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN,kernel, iterations=1)
    return opening

def closing(img):
    # define the kernel
    kernel = np.ones((3, 3), np.uint8)
    # opening the image
    closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations=1)
    return closing

def dilation(img):
    # define the kernel
    kernel = np.ones((3, 3), np.uint8)
    # invert the image
    # invert = cv2.bitwise_not(thresh)
    # dilate the image
    dilation = cv2.dilate(img, kernel, iterations=1)
    return dilation

def erosion(img):
    # define the kernel
    kernel = np.ones((5, 5), np.uint8)
    # invert the image
    # invert = cv2.bitwise_not(thresh)
    # erode the image
    erosion = cv2.erode(img, kernel,iterations=1)
    return erosion

