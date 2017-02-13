import numpy as np
import cv2

# Create a black image
img = np.zeros((512,512,1), np.uint8)
width, height, channel = img.shape
img2 = 100* np.ones((width, height, 1), np.uint8)
img3 = 100 *np.ones((width, height, 1), np.uint8)


img5 = cv2.absdiff(img2, img3)

cv2.imshow("Image", img)
cv2.imshow("img2", img2)


cv2.imshow("diff", img5)
