# P26 开闭操作
# 开操作： 去除小的干扰块
# 图像形态学的重要操作之一，基于膨胀和腐蚀操作的组合形成的
# 主要用于二值图像分析中，灰度图像亦可
# 开操作 = 腐蚀 + 膨胀， 输入图像 + 结构元素
# 闭操作：填充闭合区域
# 开操作 = 膨胀 + 腐蚀， 输入图像 + 结构元素
import cv2 as cv
import numpy as np


def open_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    cv.imshow("binary image", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (15, 1))
    binary = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)
    cv.imshow("open demo", binary)


def close_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("binary image", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (15, 15))
    binary = cv.morphologyEx(binary, cv.MORPH_CLOSE, kernel)
    cv.imshow("open demo", binary)


print("-------------hello python-----------------")
src = cv.imread("./resource/bin1.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
open_demo(src)
cv.waitKey(0)

cv.destroyAllWindows()
