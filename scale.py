import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread('testing.jpg')
half = cv2.resize(image, (0,0), fx=0.1, fy=0.1)
bigger = cv2.resize(image, (1050, 1620))
strech_mar = cv2.resize(image, (780, 540), interpolation=cv2.INTER_LINEAR)
titles = ["Original", "Half", "Bigger", "Interpolation Nearts"]
image = [image, half, bigger, strech_mar]
count = 4
for i in range(count):
    plt.subplot(2,2,i+1)
    plt.title(titles[i])
    plt.imshow(image[i])
plt.show