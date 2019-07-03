import cv2 as cv
import numpy as np


def fill_color_demo(image):
    copyImage = image.copy()
    h, w = image.shape[:2]
    mask = np.zeros([h+2, w+2], np.uint8)
    cv.floodFill(copyImage,mask,(30,30),(0,0,255),(30,30,30),(10,10,10),cv.FLOODFILL_FIXED_RANGE)
    cv.imshow("fill_color_demo",copyImage)


def fill_binary():
    image = np.zeros([400,400,3], np.uint8)
    image[100:300,100:300,:] = 255
    cv.imshow("fill binary", image)

    mask = np.ones([402, 402], np.uint8)
    mask[101:301,101:301] = 0
    cv.floodFill(image,mask,(200,200),(0,0,255),cv.FLOODFILL_FIXED_RANGE)
    cv.imshow("filled binary",image)


def abstract_face(image):
    copyImage = image.copy()
    face = copyImage[1:345, 109:392]
    gray = cv.cvtColor(face,cv.COLOR_BGR2GRAY)
    backface = cv.cvtColor(gray,cv.COLOR_GRAY2BGR)
    copyImage[1:345, 109:392] = backface
    cv.imshow("face",copyImage)


src = cv.imread("./resource/girl.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
abstract_face(src)
fill_color_demo(src)
fill_binary()
cv.waitKey(0)
cv.destroyAllWindows()
