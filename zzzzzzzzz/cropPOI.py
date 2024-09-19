import cv2

img = cv2.imread('testing.jpg')

cv2.imshow("Original Image", img)
x, y, w, h = 240,1,100,180
cropped = img[y:y+h , x:x+w]
cv2.imshow("Crop Image", cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()