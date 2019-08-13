import cv2 as cv
import numpy as np


def add_demo(m1, m2):
    dst = cv.add(m1, m2)
    cv.imshow("add_demo", dst)


def subtract_demo(m1, m2):
    dst = cv.subtract(m1, m2)
    cv.imshow("subtract_demo", dst)


def divide_demo(m1, m2):
    dst = cv.divide(m1, m2)
    cv.imshow("divide_demo", dst)


def multiply_demo(m1, m2):
    dst = cv.multiply(m1, m2)
    cv.imshow("multiply_demo", dst)


def others(m1, m2):
    M1, dev1 = cv.meanStdDev(m1) #计算矩阵的均值和标准差
    M2, dev2 = cv.meanStdDev(m2)
    print(M1)
    print(M2)
    print(dev1)
    print(dev2)


def logic_demo(m1, m2):
    dst1 = cv.bitwise_and(m1, m2)
    cv.imshow("bitwise_and", dst1)
    dst2 = cv.bitwise_or(m1, m2)
    cv.imshow("bitwise_or", dst2)
    dst3 = cv.bitwise_not(m1)
    cv.imshow("bitwise_not", dst3)
    dst4 = cv.bitwise_xor(m1, m2)
    cv.imshow("bitwise_xor", dst4)


print("----------Hello Python-------------")
src1 = cv.imread("./resource/linuxLogo.jpg")
src2 = cv.imread("./resource/windowsLogo.jpg")
print(src1.shape)
print(src2.shape)
cv.namedWindow("image1", cv.WINDOW_AUTOSIZE)
cv.namedWindow("image2", cv.WINDOW_AUTOSIZE)
cv.imshow("image1", src1)
cv.imshow("image2", src2)

# add_demo(src1, src2)
# subtract_demo(src1, src2)
# divide_demo(src1, src2)
# multiply_demo(src1, src2)
# others(src1, src2)
logic_demo(src1, src2)
cv.waitKey(0)

cv.destroyAllWindows()



