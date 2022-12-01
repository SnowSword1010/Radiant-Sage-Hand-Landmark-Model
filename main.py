# ImageFilter for using filter() function
from PIL import Image, ImageFilter
import numpy as np
import cv2
import image
import draw
import segment

# Opening the image
# (R prefixed to string in order to deal with '\' in paths)
img_path = r'/home/mayank/Downloads/WhatsApp Image 2022-11-18 at 11.16.00 PM (1).jpeg'
img = Image.open(img_path)
# img.show()
# Blurring image by sending the ImageFilter.
# GaussianBlur predefined kernel argument
filtered_img = img.filter(ImageFilter.GaussianBlur)
opencvImage = cv2.cvtColor(np.array(filtered_img), cv2.COLOR_RGB2BGR)
coordinates = np.array(image.get_coordinates(opencvImage))
print(coordinates)
# Displaying the image
filtered_img.show()
segment.edge_detection(cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR))
draw.mark_coordinates(opencvImage, coordinates)