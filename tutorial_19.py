# P22 圆检测
import cv2 as cv
import numpy as np


def detect_circles_demo(image):
    dst = cv.pyrMeanShiftFiltering(image, 10, 100)
    c_image = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
    # c_image = cv.Canny(c_image, 50, 150, apertureSize=3)
    cv.imshow("c_image", c_image)
    # 检查的圆多调大参数param2，反之同理。
    circles = cv.HoughCircles(c_image, cv.HOUGH_GRADIENT, 1, 20, param1=50, param2=24, minRadius=0, maxRadius=0)
    circles = np.uint16(np.around(circles))
    print(circles[0])
    print(circles[0].shape)
    for i in circles[0, :]:  # circle为三维数组 所以为第一个二维元素的所有元素[0,:]
        cv.circle(image, (i[0], i[1]), i[2], (0, 0, 255), 2)
        cv.circle(image, (i[0], i[1]), 2, (255, 0, 0), 2)
    cv.imshow("detect_circles_demo", image)


print("-------------hello python-----------------")
src = cv.imread("./resource/coins.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
detect_circles_demo(src)
cv.waitKey(0)

cv.destroyAllWindows()
