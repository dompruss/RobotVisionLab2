import numpy as np
import cv2

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
cv2.line(img,(0,0),(511,511),(255,0,0),5)

# draw a rectangle, green, thickness of 3 pixels
cv2.rectangle(img,(0,0),(510,128),(0,255,0),3)

#draw a circle
cv2.circle(img,(447,63), 63, (0,0,255), -1)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'CSCI 442',(10,500), font, 3,(255,255,255),2,cv2.LINE_AA)

cv2.imshow("Image", img)
