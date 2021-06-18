import cv2 as cv

image = cv.imread("e:\\attendance\\elon test.jpg")

resized_image = cv.resize(image, (400, 600))

cropped_image = image[222: , 300:]

cv.imshow("resized image", resized_image)
cv.imshow("cropped_image", cropped_image)

cv.waitKey(0)
# video = cv.VideoCapture(0)
#
# while True:
#     is_true, frame = video.read()
#
#     resized_frame = cv.resize(frame, (400, 400))
#
#     cv.imshow("Video", resized_frame)
#     cv.imshow("original video", frame)
#     cv.waitKey(1)
