import cv2 as cv
import numpy as np

image = cv.imread("e:\\attendance\\boston.jpg")
image = cv.resize(image, (660, 500))

cv.imshow("Image", image)

shifted_image = cv.warpAffine(image, np.float32([[1, 0, 45], [0, 1, -50]]), (660, 500))

rotate_mat = cv.getRotationMatrix2D((660//2, 500//2), 45, 1.0)
rotated_image = cv.warpAffine(image, rotate_mat, (660, 500))

cv.imshow("Shifted Image", shifted_image)

cv.imshow("Rotated Image", rotated_image)

cv.waitKey(0)
