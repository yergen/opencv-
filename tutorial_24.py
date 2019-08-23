# P27 其他形态学操作
# 顶帽：原图像与开操作之间的差值图像
# 黑帽：源图像与闭操作之间的差值图像
# 基本梯度：基本梯度是膨胀后的图像减去腐蚀后的图像得到差值的图像，称为
# 梯度图像中也是opencv中支持的计算形态学梯度的方法，而此方法得到的梯度
# 又被称为基本梯度。
# 内部梯度：是用原图像减去腐蚀之后的图像得到差值图像，称为图像的内部梯度
# 外部梯度：图像膨胀之后再减去原来图像得到的差值图像，称为图像的外部梯度

import cv2 as cv
import numpy as np


def hat_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    # dst = cv.morphologyEx(gray, cv.MORPH_TOPHAT, kernel)
    dst = cv.morphologyEx(gray, cv.MORPH_BLACKHAT, kernel)
    cimage = 20
    dst = cv.add(dst, cimage)
    cv.imshow("hat_demo", dst)


def hat_binary_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    # dst = cv.morphologyEx(gray, cv.MORPH_TOPHAT, kernel)
    dst = cv.morphologyEx(binary, cv.MORPH_BLACKHAT, kernel)
    cv.imshow("hat_binary_demo", dst)


def gradient_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    dst = cv.morphologyEx(binary, cv.MORPH_GRADIENT, kernel)
    cv.imshow("gradient_demo", dst)


def gradient_demo2(image):
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    dm = cv.dilate(image, kernel)
    em = cv.erode(image, kernel)
    dst1 = cv.subtract(image, em)  # internal gradient
    dst2 = cv.subtract(dm, image)  # external gradient
    cv.imshow("internal", dst1)
    cv.imshow("external", dst2)


print("-------------hello python-----------------")
src = cv.imread("./resource/girl.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
gradient_demo2(src)
cv.waitKey(0)

cv.destroyAllWindows()
