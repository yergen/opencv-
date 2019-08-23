# P23 轮廓发现
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
    edge_output = cv.Canny(gray, 30, 100)
    cv.imshow("Canny Edge", edge_output)
    return edge_output


def contours_demo(image):
    # dst = cv.GaussianBlur(image, (3, 3), 0)
    # gray = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
    # ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    # cv.imshow("binary image", binary)

    binary_canny = canny_demo(image)
    # 截图边沿有白边 方法改为RETR_TEE
    contours, heriachy = cv.findContours(binary_canny, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
        cv.drawContours(image, contours, i, (0, 0, 255), 2)
        print(i)
    cv.imshow("contour detect", image)


print("-------------hello python-----------------")
# src = cv.imread("./resource/coins.jpg")
src = cv.imread("./resource/blob.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
contours_demo(src)
cv.waitKey(0)

cv.destroyAllWindows()
