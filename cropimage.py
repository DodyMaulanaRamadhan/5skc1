import cv2

img = cv2.imread('testing.jpg')

cv2.imshow("Original Image", img)
cropped = img[1:209, 1:298]
cv2.imshow("Crop Image", cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()