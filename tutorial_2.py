import cv2 as cv
import numpy as np


def access_image(image):
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    print("height: %s,width: %s,channels: %s" % (height, width, channels))
    for row in range(height):
        for col in range(width):
            for c in range(channels):
                image[row,col,c] = 255 - image[row,col,c]
    cv.imshow("pixel_iamge",image)


def inverse(image):
    dst = cv.bitwise_not(image)
    cv.imshow("inverse image",dst)


def create_image():
    '''
    img = np.zeros([400,400,3], np.uint8)
    img[:,:,0] = np.ones([400,400])*255
    cv.imshow("new image", img)
    '''
    img = np.zeros([400,400],np.uint8)
    img[:,:] = np.ones([400,400])*127
    cv.imshow("new image", img)


src = cv.imread("./resource/girl.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
t1 = cv.getTickCount()
#access_image(src)
inverse(src)
t2 = cv.getTickCount()
print("Time = %s ms" % ((t2-t1)/cv.getTickFrequency()*1000))
cv.waitKey(0)
cv.destroyAllWindows()
