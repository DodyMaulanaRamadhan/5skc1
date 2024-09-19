import cv2

img = cv2.imread('testing.jpg')

cv2.imshow("Original Image", img)
grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale", grayscale)
cv2.waitKey(0)
cv2.destroyAllWindows()