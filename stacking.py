import cv2 as cv
import numpy as np

image = cv.imread("e:\\attendance\\boston.jpg")
elon_musk_image = cv.imread("e:\\attendance\\elon_musk.jpg")
elon_musk_image = cv.resize(elon_musk_image, (300, 410))
image = cv.resize(image, (300, 400))

hor_stack = np.vstack((image, elon_musk_image))

cv.imshow("Horizontal image", hor_stack)

cv.imshow("image", image)
cv.imshow("elon musk image", elon_musk_image)

print(elon_musk_image.shape)
print(image.shape)

cv.waitKey(0)
