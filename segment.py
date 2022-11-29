import cv2
import numpy as np

# Load in image, convert to gray scale, and Otsu's threshold
img = cv2.imread("/home/mayank/Downloads/WhatsApp Image 2022-11-18 at 11.16.00 PM (1).jpeg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow("thresh", thresh)
kernel = np.ones((3,3),np.uint8)
closing = cv2.morphologyEx(thresh,cv2.MORPH_CLOSE, kernel, iterations = 1)
dist = cv2.distanceTransform(closing, cv2.DIST_L2, 3)
ret, dist1 = cv2.threshold(dist, 0.6*dist.max(), 255, 0)
cv2.imshow("dist1", dist1)
markers = np.zeros(dist.shape, dtype=np.int32)
dist_8u = dist1.astype('uint8')
contours, _ = cv2.findContours(dist_8u, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for i in range(len(contours)):
    cv2.drawContours(markers, contours, i, (i+1), -1)
markers = cv2.circle(markers, (15,15), 5, len(contours)+1, -1)
markers = cv2.watershed(img, markers)
img[markers == -1] = [0,0,255]
cv2.imshow("Image", img)
cv2.waitKey(0)