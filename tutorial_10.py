import cv2 as cv
import numpy as np


def equalhist_demo(image):   #直方图均衡化
    gray =cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    dst = cv.equalizeHist(gray)
    cv.imshow("equalHist_demo", dst)


def clahe_demo(image):  #局部自适应的直方图均衡化
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    clahe = cv.createCLAHE(clipLimit=5.0, tileGridSize=(8, 8))
    dst = clahe.apply(gray)
    cv.imshow("clahe_demo", dst)


def create_rgb_hist(image): #创建RGB直方图
    h, w, c = image.shape
    rgbHist = np.zeros([16*16*16, 1], np.float32)
    bsize = 256 / 16
    for row in range(h):
        for col in range(w):
            b = image[row, col, 0]
            g = image[row, col, 1]
            r = image[row, col, 2]
            index = np.int(b/bsize)*16*16+np.int(g/bsize)*16 + np.int(r/bsize)
            rgbHist[index, 0] += 1
    return rgbHist


def compare_hist(image1,image2):
    hist1 = create_rgb_hist(image1)
    hist2 = create_rgb_hist(image2)
    match1 = cv.compareHist(hist1,hist2,cv.HISTCMP_BHATTACHARYYA)
    match2 = cv.compareHist(hist1,hist2,cv.HISTCMP_CORREL)
    match3 = cv.compareHist(hist1,hist2,cv.HISTCMP_CHISQR)
    print("巴氏距离：%s，相关性：%s, 卡方：%s" %(match1,match2,match3))



print("-------------hello python-----------------")
# src = cv.imread("./resource/rice.jpg")
# cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
# cv.imshow("input image", src)
image1 = cv.imread("./resource/lena.jpg")
iamge2 = cv.imread("./resource/lenanoise.jpg")
cv.imshow("image1",image1)
cv.imshow("image2",iamge2)
compare_hist(image1,iamge2)
# equalhist_demo(src)
# clahe_demo(src)
cv.waitKey(0)

cv.destroyAllWindows()