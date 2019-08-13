import cv2 as cv
import numpy as np


def threshold_demo(image):  # 全局阈值
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary1 = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    _, binary2 = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_TRIANGLE)
    print("threshold value: %s" % ret)
    cv.imshow("binary_OTSU image", binary1)
    cv.imshow("binary_TRIANGLE image", binary2)


def local_threshold(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    # binary = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 15, 10)
    binary = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 15, 10)
    cv.imshow("binary image", binary)


def custom_threshold(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    h, w = image.shape[:2]
    m = np.reshape(gray, [1, w * h])
    mean = m.sum() / (h * w)
    # mean = gray.mean()
    print("gray mean: %s" % mean)
    _, binary = cv.threshold(gray, mean, 255, cv.THRESH_BINARY)
    cv.imshow("binary image", binary)


print("-------------hello python-----------------")
src = cv.imread("./resource/girl.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
custom_threshold(src)
cv.waitKey(0)

cv.destroyAllWindows()
