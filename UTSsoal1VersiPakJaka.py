import cv2
import numpy as np
image1 = cv2.imread('testing.jpg')
img = cv2.cvtColor(image1, cv2.COLOR_GRAY2BGR)
ret, treshold = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow('Otsu Threshold', treshold)
cv2.waitKey(0)
cv2.destroyAllWindows()

