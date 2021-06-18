import cv2 as cv

image = cv.imread("e:\\attendance\\elon test.jpg")

image= cv.resize(image, (400, 600))

# cv.rectangle(image, (100, 100), (300, 300), (0, 0, 255), thickness=2)
#
# cv.circle(image, (100, 100), 80, (255, 0, 0), thickness=3)
#
# cv.line(image, (50, 50), (100, 300), (0, 255, 0), thickness=3)

cv.putText(image, "Elon Musk", (100, 100), cv.FONT_ITALIC, 1,
           (255, 0, 0), thickness=2)

cv.putText(image, "Elon Musk 2", (200, 200), cv.FONT_ITALIC, 1,
           (255, 255, 0), thickness=2)
cv.imshow("Image", image)
cv.waitKey(0)
