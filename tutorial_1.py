import cv2 as cv
import numpy as np


def video_demo():
    capture = cv.VideoCapture(0)
    while True:
        ret, frame = capture.read()
        frame = cv.flip(frame, 1) #镜像
        cv.imshow("video", frame)
        key = cv.waitKey(50)  #ms
        if key == 27:
            break


def get_image_info(image):
    print(type(image))
    print(image.shape)
    print(image.size)
    print(image.dtype)
    pixel_data = np.array(image)
    print(pixel_data)


print("----------Hello Python-------------")
src = cv.imread("./resource/girl.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
get_image_info(src)
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
cv.imwrite("./resource/gray.png", gray)
video_demo()                #show video
cv.waitKey(0)
cv.destroyAllWindows()

