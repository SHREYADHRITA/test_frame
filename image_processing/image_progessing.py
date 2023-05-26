import cv2
import numpy as np

FILE_NAME = 'picture.JPG'
img = cv2.imread(FILE_NAME)


def resize_img():
    try:
        (height, width) = img.shape[:2]
        res = cv2.resize(img, (int(width / 2), int(height / 2)), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite('result1.jpg', res)

    except IOError:
        print('Error while reading files')


def rotate_img():

    try:
        (rows, cols) = img.shape[:2]
        im = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)
        res = cv2.warpAffine(img, im, (cols, rows))
        cv2.imwrite('result2.jpg', res)
    except IOError:
        print('Error while reading files')


def transfer_img():
    try:
        (rows, cols) = img.shape[:2]
        txr = np.float32([[1, 0, 200], [0, 1, 200]])
        res = cv2.warpAffine(img, txr, (cols, rows))
        cv2.imwrite('result3.jpg', res)

    except IOError:
        print('Error while reading files')


def edge_only_img():
    try:
        edges = cv2.Canny(img, 100, 200)
        cv2.imwrite('result4.jpg', edges)
    except IOError:
        print('Error while reading files !!!')


edge_only_img()
transfer_img()
rotate_img()
resize_img()
