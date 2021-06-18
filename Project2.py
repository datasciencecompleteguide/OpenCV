import cv2 as cv
from tensorflow import keras
import numpy as np

model = keras.models.load_model("densenet121_detection_model.h5")

haar_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")

label_dict = {0: "Without Mask", 1: "With Mask"}
color_dict = {0: (0, 0, 255), 1: (0, 255, 0)}

video = cv.VideoCapture(0)

while True:
    is_true, frame = video.read()
    flipped_image = cv.flip(frame, 1, 1)

    face_detect = haar_cascade.detectMultiScale(flipped_image)
    for x, y, w, h in face_detect:

        face = flipped_image[y:y+h, x:x+w]
        face = cv.resize(face, (224, 224))

        normalization = face/255.0
        reshaped_image = np.reshape(normalization, (1, 224, 224, 3))
        stack = np.vstack([reshaped_image])

        result = model.predict(stack)

        if (result[0][0]) > result[0][1]:
            percent = round(result[0][0]*100, 2)
        else:
            percent = round(result[0][1]*100, 2)

        label = np.argmax(result, axis=1)[0]

        cv.rectangle(flipped_image, (x, y), (x+w, y+h), color_dict[label], thickness=2)
        cv.rectangle(flipped_image, (x, y-40), (x+w, y), color_dict[label], thickness=cv.FILLED)
        cv.putText(flipped_image, label_dict[label] + " " + str(percent) + "%", (x, y-10),
                   cv.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), thickness=2)

    cv.imshow("Face Mask Detection", flipped_image)
    cv.waitKey(10)

