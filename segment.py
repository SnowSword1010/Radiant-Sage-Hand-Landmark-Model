import cv2
import numpy as np
import matplotlib as plt

def image_processing(image):
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    # BINARISE THE IMAGE
    ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    cv2.imshow("thresh", thresh)
    # DENOISING THRESH
    img1 = cv2.fastNlMeansDenoising(thresh, None, 30.0, 7, 10)
    cv2.imshow("denoised", img1)
    # CANNY EDGE
    edges = cv2.Canny(img1,100,200)
    cv2.imshow("Canny", edges)
    # FINDING CONTOURS
    # Use a copy of the image e.g. edged.copy()
    # since findContours alters the image
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cv2.imshow('Canny Edges After Contouring', edges)
    print("Number of Contours found = " + str(len(contours)))
    # Draw all contours
    # -1 signifies drawing all contours
    cv2.drawContours(image, contours, -1, (0, 255, 0), 3)
    cv2.imshow('Contours', image)