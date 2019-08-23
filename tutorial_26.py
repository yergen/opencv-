import cv2 as cv
import numpy as np


def face_detect_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    face_detector = cv.CascadeClassifier("")  # 缺少人脸检测文件
    faces = face_detector.detectMultiScale(gray, 1.02, 5)
    for x, y, w, h in faces:
        cv.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv.imshow("result", image)


print("-------------hello python-----------------")
# src = cv.imread("./resource/girl.jpg")
capture = cv.VideoCapture(0)
while True:
    ret, frame = capture.read()
    frame = cv.flip(frame, 1)
    face_detect_demo(frame)
    i = cv.waitKey(10)
    if i == 27:
        break


cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.namedWindow("result", cv.WINDOW_AUTOSIZE)
# cv.imshow("input image", src)
# face_detect_demo(src)
cv.waitKey(0)

cv.destroyAllWindows()
