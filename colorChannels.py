import cv2 as cv
import numpy as np

image = cv.imread("e:\\attendance\\boston.jpg")
image = cv.resize(image, (660, 500))

blank = np.zeros(image.shape[:2], dtype=np.uint8)

cv.imshow("image", image)

r = image[:, :, 0]
g = image[:, :, 1]
b = image[:, :, 2]

red_image = cv.merge([blank, blank, r])
green_image = cv.merge([blank, g, blank])
blue_image = cv.merge([b, blank, blank])

cv.imshow("green image channel", green_image)
cv.imshow("Red Image Channel", red_image)
cv.imshow("blue image channel", blue_image)

cv.imshow("red image", r)
cv.imshow("green image", g)
cv.imshow("blue image", b)

cv.waitKey(0)
