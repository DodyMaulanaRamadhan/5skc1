import cv2
from PIL import Image

image = Image.open('testing.jpg')

image.show()
cropped = (250, 250, 300, 400)
img_crop = image.crop(cropped)
img_crop.show()