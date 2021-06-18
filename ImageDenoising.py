# import cv2 as cv
#
# image = cv.imread("e:\\attendance\\elon test.jpg")
# image = cv.resize(image, (500, 660))
#
# gray_image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
#
# noise = cv.imread("e:\\attendance\\noise.png")
# noised_image = cv.bitwise_or(image, noise)
#
# cv.imshow("Noised image", noised_image)
#
# Denoised_image = cv.fastNlMeansDenoising(gray_image, None, 10, 7, 7)
# cv.imshow("Denoised Image", Denoised_image)
# cv.waitKey(0)
# import autopy
#
# def hello():
#     autopy.alert.alert("Hello, World")
# hello()
#
# autopy.mouse.smooth_move(1, 1)
import math
import time
import random
import sys
import autopy

TWO_PI = math.pi * 2.0


def sine_mouse_wave():
    width, height = autopy.screen.size()
    height /= 2
    height -= 10  # Stay in the screen bounds.

    for x in range(int(width)):
        y = int(height * math.sin((TWO_PI * x) / width) + height)
        autopy.mouse.move(x, y)
        time.sleep(random.uniform(0.001, 0.003))


sine_mouse_wave()

autopy.key.type_string("Hello, World", wpm=10)