import cv2 as cv
import numpy as np


# Reduce = 高斯模糊 + 降采样
# Expand = 扩大 + 卷积
# 拉普拉斯金字塔 L1 = G1 - expand(G2)
# 图像的长宽必须相等且为2的n次方
def pyramid_demo(image):
    level = 3
    temp = image.copy()
    pyramid_images = []
    for i in range(level):
        dst = cv.pyrDown(temp)
        pyramid_images.append(dst)
        cv.imshow("pyramid_" + str(i), dst)
        temp = dst.copy()
    return pyramid_images


def lapalian_demo(image):
    images = pyramid_demo(image)
    level = len(images)
    for i in range(level - 1, -1, -1):
        print(i)
        if i > 0:
            expand = cv.pyrUp(images[i], dstsize=images[i - 1].shape[:2])
            lpls = cv.subtract(images[i - 1], expand)
            cv.imshow("lapalian_" + str(i), lpls)
        else:
            expand = cv.pyrUp(images[i], dstsize=image.shape[:2])
            lpls = cv.subtract(image, expand)
            cv.imshow("lapalian_" + str(i), lpls)


print("-------------hello python-----------------")
src = cv.imread("./resource/lena.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
lapalian_demo(src)
cv.waitKey(0)

cv.destroyAllWindows()
