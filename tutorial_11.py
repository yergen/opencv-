import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def back_project_demo():
    sample = cv.imread("./resource/sample.jpg")
    target = cv.imread("./resource/target.jpg")
    roi_hsv = cv.cvtColor(sample, cv.COLOR_BGR2HSV)
    target_hsv = cv.cvtColor(target, cv.COLOR_BGR2HSV)

    # show image
    cv.imshow("sample", sample)
    cv.imshow("target", target)

    # 计算直方图并正则化
    roi_hist = cv.calcHist([roi_hsv], [0, 1], None, [32, 32], [0, 180, 0, 256])
    cv.normalize(roi_hist, roi_hist, 0, 255, cv.NORM_MINMAX)
    dst = cv.calcBackProject([target_hsv], [0, 1], roi_hist, [0, 180, 0, 256], 1)
    cv.imshow("back_project_demo", dst)


def hist2D_demo(image):
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    hist = cv.calcHist(hsv, (0, 1), None, (32, 32), (0, 180, 0, 256))
    # cv.imshow("hist2D_demo", hist)
    plt.imshow(hist, interpolation='nearest')
    plt.title("2D Histgram")
    plt.show()


print("-------------hello python-----------------")
src = cv.imread("./resource/girl.jpg")
# cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
# cv.imshow("input image", src)
hist2D_demo(src)
# back_project_demo()
cv.waitKey(0)


cv.destroyAllWindows()
