import cv2 as cv

image = cv.imread("e:\\attendance\\multiple_faces.png")
image = cv.resize(image, (600, 600))

image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)

haar_cascade = cv.CascadeClassifier("C:\\Users\\HP\\AppData\\Local\\Programs\\"
                                    "Python\\Python38\\Lib\\site-packages"
                                    "\\cv2\\data\\haarcascade_frontalface_alt.xml")


face_detect = haar_cascade.detectMultiScale(image, minNeighbors=7, scaleFactor=2)

print(*face_detect)

for x, y, w, h in face_detect:
    cv.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), thickness=2)


cv.imshow("Image", image)
cv.waitKey(0)
