# 图像形态学
# 是图像处理学科中的单独一个学个
# 灰度和二值图像处理中的重要手段
# 是由数学的集合论等相关理论发展起来的
# - 膨胀 n*n 结构模板 最大值替换中心像素
# 膨胀的作用：1.对象大小增加一个元素 2.平滑对象边缘 3.减少或填充对象之间的距离
# - 腐蚀 n*n 结构模板 最小值替换中心像素
import cv2 as cv
import numpy as np


def erode_demo(image):  # 腐蚀
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    cv.imshow("binary image", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    dst = cv.erode(binary, kernel)
    cv.imshow("erode_demo", dst)


def dilate_demo(image): # 膨胀
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("binary image", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (11, 11))
    dst = cv.dilate(binary, kernel)
    cv.imshow("dilate_demo", dst)


print("-------------hello python-----------------")
src = cv.imread("./resource/girl.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
# dilate_demo(src)
kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
dst = cv.dilate(src, kernel)
cv.imshow("erode_demo", dst)
cv.waitKey(0)

cv.destroyAllWindows()
