import cv2 as cv
import numpy as np

blank = np.zeros((500, 500), dtype=np.uint8)
blank1 = np.zeros((500, 500), dtype='uint8')

circle_image = cv.circle(blank, (250, 250), 250, (255, 255, 255), thickness=cv.FILLED)

rectangle_image = cv.rectangle(blank1, (50, 50), (450, 450), (255, 255, 255),
                               thickness=cv.FILLED)

cv.imshow("Circle", circle_image)
cv.imshow("Rectangle", rectangle_image)

# Bitwise And

and_image = cv.bitwise_and(circle_image, rectangle_image)
cv.imshow("and image", and_image)

# Bitwise Or
or_image = cv.bitwise_or(circle_image, rectangle_image)
cv.imshow("or image", or_image)

# Bitwise Not
not_image = cv.bitwise_not(rectangle_image)
cv.imshow("Not Image", not_image)

# Bitwise Xor
xor_image = cv.bitwise_xor(circle_image, rectangle_image)
cv.imshow("Xor Image", xor_image)
cv.waitKey(0)
