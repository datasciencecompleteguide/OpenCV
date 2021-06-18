import cv2 as cv
import matplotlib.pyplot as plt

image = cv.imread("e:\\attendance\\boston.jpg")
image = cv.resize(image, (660, 500))

cv.imshow("Original Image", image)

# bgr_image = cv.cvtColor(image, cv.COLOR_RGB2BGR)
# cv.imshow("Bgr_image", bgr_image)
#
# hsv_image = cv.cvtColor(image, cv.COLOR_RGB2HSV)
#
# cv.imshow("hsv image", hsv_image)
#
# lab_image = cv.cvtColor(image, cv.COLOR_RGB2Lab)
# cv.imshow("lab image", lab_image)
#
# LAB_image = cv.cvtColor(image, cv.COLOR_RGB2LAB)
# cv.imshow("LAB Imgae", LAB_image)


plt.imshow(image)

plt.show()
cv.waitKey(0)