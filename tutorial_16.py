# P19图像梯度
# 一阶导数和soble算子
# 二阶导数和拉普拉斯算子

import cv2 as cv
import numpy as np


def sobel_demo(image):
    # grad_x = cv.Sobel(image, cv.CV_32F, 1, 0)
    # grad_y = cv.Sobel(image, cv.CV_32F, 0, 1)
    grad_x = cv.Scharr(image, cv.CV_32F, 1, 0)
    grad_y = cv.Scharr(image, cv.CV_32F, 0, 1)
    # dst = (unchar)saturate(alpha*src + beta)
    gradx = cv.convertScaleAbs(grad_x)
    grady = cv.convertScaleAbs(grad_y)
    cv.imshow("grad_x", gradx)
    cv.imshow("grad_y", grady)

    gradxy = cv.addWeighted(gradx, 0.5, grady, 0.5, 0)
    cv.imshow("grad_xy", gradxy)


def lapalian_demo(image):
    # dst = cv.Laplacian(image, cv.CV_32F)
    # lpls = cv.convertScaleAbs(dst)
    kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    dst = cv.filter2D(image, cv.CV_32F, kernel=kernel)
    dst = cv.convertScaleAbs(dst)
    # cv.imshow("lapalian_demo", lpls)
    cv.imshow("lapalian_demo", dst)


print("-------------hello python-----------------")
src = cv.imread("./resource/girl.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
lapalian_demo(src)
cv.waitKey(0)

cv.destroyAllWindows()
