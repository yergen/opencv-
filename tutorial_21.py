# P24对象测量
# approPolyDP -contour -epsilon 越小越折线越逼近真实形状 -close 是否为闭合区域

import cv2 as cv
import numpy as np


def measure_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("binary image", binary)
    print("Thresh value: %s" % ret)
    contours, hireachy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
        area = cv.contourArea(contour)  # 轮廓面积
        x, y, w, h = cv.boundingRect(contour)  # 外接矩形
        rate = min(w, h) / max(w, h)
        print(rate)
        mm = cv.moments(contour)  # 几何矩
        print(type(mm))
        cx = mm['m10'] / mm['m00']
        cy = mm['m01'] / mm['m00']
        # cv.circle(image, (np.int(cx), np.int(cy)), 3, (0, 255, 255), -1)
        # cv.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        print("contour area: %s" % area)
        approxCurve = cv.approxPolyDP(contour, 4, True)
        print(approxCurve.shape)
        if approxCurve.shape[0] > 6:
            cv.drawContours(image, contours, i, (0, 0, 255), 3)
        elif approxCurve.shape[0] == 4:
            cv.drawContours(image, contours, i, (0, 255, 255), 3)
        elif approxCurve.shape[0] == 3:
            cv.drawContours(image, contours, i, (0, 100, 100), 3)
    cv.imshow("measure contours", image)


print("-------------hello python-----------------")
src = cv.imread("./resource/blob.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
measure_demo(src)
cv.waitKey(0)

cv.destroyAllWindows()
