# P20 Canny边缘提取
# 1. 高斯模糊-GaussianBlur
# 2. 灰度转换-cvtColor
# 3. 计算梯度-Sobel/Scharr
# 4. 非最大信号抑制
#    Sobel算子，theta = artant(Gv/Gz)
# 5. 高低阈值输出高低图像
#    T2:T1 = 2:1 / 3:1 其中T2为高阈值，T1为低阈值
import cv2 as cv
import numpy as np


def canny_demo(image):
    blurred = cv.GaussianBlur(image, (3, 3), 0)  # 1 降噪
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)  # 2
    # X Gradiant
    xgrad = cv.Sobel(gray, cv.CV_16SC1, 1, 0)
    # Y Gradiant
    ygrad = cv.Sobel(gray, cv.CV_16SC1, 0, 1)
    # Edge
    # edge_output = cv.Canny(xgrad, ygrad, 50, 150)
    edge_output = cv.Canny(gray, 50, 150)
    cv.imshow("Canny Edge", edge_output)

    dst = cv.bitwise_and(image, image, mask=edge_output)
    cv.imshow("Canny Color Edge", dst)


print("-------------hello python-----------------")
src = cv.imread("./resource/girl.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
canny_demo(src)
cv.waitKey(0)

cv.destroyAllWindows()
