# ImageFilter for using filter() function
from PIL import Image, ImageFilter
import numpy as np
import cv2
import image
import draw
import segment

# returns the coordinates of mediapipe hand landmarks
def get_coordinates(img_path):
    img = Image.open(img_path)
    # Applying gaussian blur to the image
    filtered_img = img.filter(ImageFilter.GaussianBlur)
    # changing the image to one that can be processed by opencv
    opencvImage = cv2.cvtColor(np.array(filtered_img), cv2.COLOR_RGB2BGR)
    # getting mediapipe hand landmark coordinates
    coordinates = np.array(image.get_coordinates(opencvImage))
    print(coordinates)
    # Displaying the image
    filtered_img.show()
    # marking the coordinates received on original image
    draw.mark_coordinates(opencvImage, coordinates)
    # Detecting contours on the image and displaying various image processing stages
    segment.image_processing(cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR))
    # press esacpe key to exit all windows
    while(1):
        k = cv2.waitKey(33)
        if k==27:  # Esc key to stop
            break
        elif k==-1: # normally -1 returned,so don't print it
            continue
    return coordinates