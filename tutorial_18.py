# P21 直线检测
import cv2 as cv
import numpy as np


def line_detection(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    edge = cv.Canny(gray, 30, 90, apertureSize=3)
    cv.imshow("Canny image", edge)
    lines = cv.HoughLines(edge, 1, np.pi / 180, 140)
    for line in lines:
        print(type(line))
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = rho * a
        y0 = rho * b
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * a)
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * a)
        cv.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
    cv.imshow("line_detection", image)


def line_detection_possible_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    edge = cv.Canny(gray, 50, 100, apertureSize=3)
    cv.imshow("Canny image", edge)
    lines = cv.HoughLinesP(edge, 1, np.pi / 180, 100, minLineLength=50, maxLineGap=10)
    for line in lines:
        print(type(line))
        x1, y1, x2, y2 = line[0]
        cv.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
    cv.imshow("line_dectection_possible_demo", image)


print("-------------hello python-----------------")
src = cv.imread("./resource/sudu.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
line_detection_possible_demo(src)
cv.waitKey(0)

cv.destroyAllWindows()
