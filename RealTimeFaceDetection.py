import cv2 as cv

video = cv.VideoCapture(0)


haar_cascade = cv.CascadeClassifier("C:\\Users\\HP\\AppData\\Local\\Programs\\"
                                    "Python\\Python38\\Lib\\site-packages"
                                    "\\cv2\\data\\haarcascade_frontalface_alt.xml")


while True:
    is_true, frame = video.read()

    frame = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
    face_detect = haar_cascade.detectMultiScale(frame)
    for x, y, w, h in face_detect:
        cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), thickness=2)

    cv.imshow("Image", frame)
    cv.waitKey(1)
