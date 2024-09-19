import cv2
image = cv2.imread('testing.jpg')
height, width = image.shape[:2]
center = (width/2, height/2)
angle = 45
scale = 1
rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)
rotation_image = cv2.warpAffine(image, rotation_matrix,(width, height))
cv2.imwrite("OutputImageRotateOpenCV.jpg", rotation_image)