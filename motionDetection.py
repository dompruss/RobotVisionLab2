import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cv2.namedWindow("Video")
#cv2.namedWindow("Img1")
#cv2.namedWindow("GreyScale")
cv2.namedWindow("Blobby")
_,f=cap.read()
avg1 = np.float32(f);

while True:
    _,f=cap.read()
    status, img = cap.read()
    blur = cv2.blur(img,(5,5))
    cv2.imshow("Video",img)
    
    grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.accumulateWeighted(blur,avg1,0.5)
    
    res1 = cv2.convertScaleAbs(avg1)

    diff = cv2.absdiff( blur,res1)
    diff = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)

    
    ret,diff = cv2.threshold(diff,15,255,0)
    diff = cv2.dilate(diff, None, iterations=2)
    im2, contours, hierarchy = cv2.findContours(diff,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    
    
    
    for c in contours:
        if cv2.contourArea(c) < 1500:
            continue
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(f, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    cv2.imshow("Video",f)
    #cv2.imshow("Img1",blur)
    #cv2.imshow("avg1",res1)
    #cv2.imshow("GreyScale",grey)
    cv2.imshow("Blobby", diff)
    k=cv2.waitKey(1)
    if k==27:
        break
cv2.destroyAllWindows()
