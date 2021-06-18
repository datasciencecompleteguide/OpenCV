import cv2 as cv

image = cv.imread("e:\\attendance\\boston.jpg")
image = cv.resize(image, (660, 500))


cv.imshow("image", image)


# Normal Average Blur
Average_blur = cv.blur(image, (7, 7))
cv.imshow("Average blur", Average_blur)

# Gaussian Blur
gauss_blur = cv.GaussianBlur(image, (7, 7), 15)
cv.imshow("Gaussian Blur", gauss_blur)

# Median Blur
median_blur = cv.medianBlur(image, 5)
cv.imshow("Median Blur", median_blur)

# Bilateral Filter

bilateral_image = cv.bilateralFilter(image, 3, 255, 24)
cv.imshow("Bilateral image", bilateral_image)

cv.waitKey(0)
