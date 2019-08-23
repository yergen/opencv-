# P28 分水岭算法
# 流程：输入图像->灰度->二值化->距离变换
# ->寻找种子->生成Marker->分水岭变换->输出图像

import cv2 as cv
import numpy as np


def water_demo(image):
    print(image.shape)
    blurred = cv.pyrMeanShiftFiltering(image, 10, 100)  # 均值偏移滤波
    # gray/binary image
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("binary image", binary)

    # marphylogy operation
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    mb = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel, iterations=2)
    sure_bg = cv.dilate(mb, kernel, iterations=3)
    cv.imshow("mor-opt", sure_bg)

    # distance transform
    dist = cv.distanceTransform(mb, cv.DIST_L2, 3)
    dist_output = cv.normalize(dist, 0, 1.0, cv.NORM_MINMAX)
    cv.imshow("distance transform", dist_output * 50)

    # 寻找种子
    ret, surface = cv.threshold(dist, dist.max() * 0.6, 255, cv.THRESH_BINARY)
    cv.imshow("surface-bin", surface)

    surface_fg = np.uint8(surface)
    unknow = cv.subtract(sure_bg, surface_fg)
    cv.imshow("unknow", unknow)
    ret, markers = cv.connectedComponents(surface_fg)
    print(ret)

    # watershed transform
    markers = markers + 1
    markers[unknow == 255] = 0
    markers = cv.watershed(src, markers)
    src[markers == -1] = [0, 0, 255]
    cv.imshow("result", src)


print("-------------hello python-----------------")
src = cv.imread("./resource/coins.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
water_demo(src)
cv.waitKey(0)

cv.destroyAllWindows()
