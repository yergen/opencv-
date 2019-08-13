import cv2 as cv
import numpy as np


def extract_object_demo():
    capture = cv.VideoCapture("E:/Opencv/resource/video.mp4")
    while True:
        ret, frame = capture.read()
        if not ret:
            break
        cv.imshow("video", frame)
        key = cv.waitKey(40)
        if key == 27:
            break


def color_space_demo(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    hsv = cv.cvtColor(image,cv.COLOR_BGR2HSV)
    yuv = cv.cvtColor(image,cv.COLOR_BGR2YUV)
    Ycrcb = cv.cvtColor(image,cv.COLOR_BGR2YCrCb)
    cv.imshow("gray",gray)
    cv.imshow("hsv",hsv)
    cv.imshow("yuv",yuv)
    cv.imshow("ycrcb",Ycrcb)


src = cv.imread("./resource/girl.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)

# b, g, r = cv.split(src)     #分离通道
# cv.imshow("channel b", b)
# cv.imshow("channel g", g)
# cv.imshow("channel r", r)
#
# src = cv.merge([b,g,r])     #合并通道
# src[:,:,0] = 0
# cv.imshow("change image", src)
#print(np.array(src))
#color_space_demo(src)
extract_object_demo()

cv.waitKey(0)
cv.destroyAllWindows()
