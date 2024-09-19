import cv2
image1 = cv2.imread('testing.jpg')
t_lower = 50
t_upper = 150
aperture_size = 5
L2GRadient = True
edge = cv2.Canny(image1, t_lower, t_upper)
edge_aperture = cv2.Canny(image1, t_lower, t_upper, apertureSize=aperture_size)
edgeL2 = cv2.Canny(image1, t_lower, t_upper, L2gradient=L2GRadient)
cv2.imshow('Edge Default Canny', edge)
cv2.imshow('Edge Aperture Canny', edge_aperture)
cv2.imshow('Edge Gradient Canny', edgeL2)
cv2.waitKey(0)
cv2.destroyAllWindows()
