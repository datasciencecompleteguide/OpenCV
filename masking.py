import cv2 as cv
import numpy as np

image = cv.imread("e:\\attendance\\puppies.jpg")
image = cv.resize(image, (800, 600))

blank = np.zeros(image.shape[:2], dtype=np.uint8)

# circle = cv.circle(blank, (800//2 + 140, 600//2), 200, (255, 255, 255), thickness=cv.FILLED)

rectangle = cv.rectangle(blank.copy(), (50, 50), (600, 400),
                         (25, 0, 0), thickness=-1)

cv.imshow("puppies image", image)
# cv.imshow("Circle image", circle)
cv.imshow("Rectangle", rectangle)

masked_image = cv.bitwise_or(image, image, mask=rectangle)

cv.imshow("masked image", masked_image)


cv.waitKey(0)
