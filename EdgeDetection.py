import cv2 as cv
import numpy as np

image = cv.imread("e:\\attendance\\puppies.jpg")
image = cv.resize(image, (800, 600))

gray_image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)

cv.imshow("Image", image)
cv.imshow("Gray Image", gray_image)

# Laplacian Edge Detector

lap = cv.Laplacian(gray_image, cv.CV_32F)
lap = np.uint8(np.absolute(lap))

# Sobel Edge Detector
sobel_x = cv.Sobel(gray_image, cv.CV_64F, 1, 0)
sobel_y = cv.Sobel(gray_image, cv.CV_64F, 0, 1)

cv.imshow("Sobel X", sobel_x)
cv.imshow("Sobel Y", sobel_y)

Sobel = cv.bitwise_or(sobel_x, sobel_y)
cv.imshow("Sobel Combined", Sobel)

# Canny Edge Detector
canny_image = cv.Canny(gray_image, 25, 255)

cv.imshow("Canny Edge ", canny_image)
cv.imshow("Laplacian", lap)
cv.waitKey(0)
