import cv2 as cv
import numpy as np


def blur_demo(image):           #均值模糊
    dst = cv.blur(image,(5,1))  #水平和垂直模糊
    cv.imshow("blur_demo",dst)


def media_blur_demo(image):         #中值模糊
    dst = cv.medianBlur(image,5)    #去噪点噪声
    cv.imshow("media_blur_demo",dst)


def custom_blur_demo(image):     #自定义模糊
    #kernel = np.ones([5,5], np.float32)/25
    #kernel = np.array([[1,1,1],[1,1,1],[1,1,1]],np.float32)/9
    #总和为0：边缘梯度，总和为1：增强 算子一般为奇数
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)
    dst = cv.filter2D(image,-1,kernel = kernel)
    cv.imshow("custom_blur_demo", dst)


src = cv.imread("./resource/girl.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
blur_demo(src)
media_blur_demo(src)
custom_blur_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()

