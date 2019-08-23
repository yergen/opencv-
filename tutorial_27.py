# P30 Opencv_Tessert-OCR
# 预处理
#  去除干扰线和点，不同的结构元素中选择，
#  image与numpy array相互转化，识别和输出。
#
import cv2 as cv
import numpy as np
from PIL import Image
import pytesseract as tess


def recognize_text():
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (2, 2))
    bin1 = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (2, 1))
    open_out = cv.morphologyEx(bin1, cv.MORPH_OPEN, kernel)
    cv.imshow("binary image", open_out)

    textImage = Image.fromarray(open_out)
    text = tess.image_to_string(textImage)
    print("识别结果: %s", text)


print("-------------hello python-----------------")
src = cv.imread("./resource/number.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
recognize_text()
cv.waitKey(0)

cv.destroyAllWindows()
