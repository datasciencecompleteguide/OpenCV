import cv2 as cv
import numpy as np

# 1 creating the blank image or canvas
# blank_image = np.zeros((400, 400), dtype='uint8')
#
# cv.imshow("image", blank_image)

image = cv.imread("e:\\attendance\\boston.jpg")

image = cv.resize(image, (660, 600))

gray_image = cv.cvtColor(image, cv.COLOR_RGB2BGR)

cv.imshow("Boston image", image)
cv.imshow("Gray Image", gray_image)

# Blurring the image

blurred_image = cv.GaussianBlur(image, (3, 3), 15)

cv.imshow("Blurred Image", blurred_image)

# Canny Edge Detector

canny_image = cv.Canny(image, 255, 255)

cv.imshow("Canny Edge Image", canny_image)
cv.waitKey(0)
