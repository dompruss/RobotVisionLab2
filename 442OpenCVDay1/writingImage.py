import numpy as np
import cv2 as cv

cv.namedWindow("Image")

img = cv.imread("japaneseflowers.jpg", cv.IMREAD_COLOR)

cv.imshow("Image", img)

cv.imwrite('flowersConvert.png',img)
