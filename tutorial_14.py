import cv2 as cv
import numpy as np


def big_threshold(image):
    print(image.shape)
    cw = 25
    ch = 25
    h, w = image.shape[:2]
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    for row in range(0, h, ch):
        for col in range(0, w, cw):
            roi = gray[row:row + cw, col:col + ch]
            binary = cv.adaptiveThreshold(roi, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 127, 20)
            gray[row:row + cw, col:col + ch] = binary
            print(np.std(binary),np.mean(binary))
    cv.imshow("binary image", gray)


print("-------------hello python-----------------")
src = cv.imread("./resource/girl.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
big_threshold(src)
cv.waitKey(0)

cv.destroyAllWindows()
