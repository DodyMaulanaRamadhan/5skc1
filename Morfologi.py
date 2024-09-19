import cv2
import numpy as np
image1 = cv2.imread('testing.jpg',0)
kernel = np.ones((5,5), np.uint8)
img_erosion = cv2.erode(image1, kernel, iterations=1)
img_dilation = cv2.dilate(image1, kernel, iterations=1)
cv2.imshow('Erosion', img_erosion)
cv2.imshow('Dilation', img_dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()