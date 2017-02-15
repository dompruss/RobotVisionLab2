import cv2
import numpy as np

def updateRedMin(x):
    global redMin
    redMin = x
def updateRedMax(x):
    global redMax
    redMax = x
def updateGreenMin(x):
    global greenMin
    greenMin = x
def updateGreenMax(x):
    global greenMax
    greenMax = x
def updateBlueMin(x):
    global blueMin
    blueMin = x
def updateBlueMax(x):
    global blueMax
    blueMax =x

cap = cv2.VideoCapture(0)
cv2.namedWindow("Video")
cv2.namedWindow("Sliders")
cv2.namedWindow("HSV")
cv2.namedWindow("Color Finder")
redMin=0
blueMin=0
greenMin=0
redMax=255
blueMax=255
greenMax=255
# create trackbars for color change
cv2.createTrackbar('Rmin','Sliders',0,255,updateRedMin)
cv2.createTrackbar('Rmax','Sliders',255,255,updateRedMax)
cv2.createTrackbar('Gmin','Sliders',0,255,updateGreenMin)
cv2.createTrackbar('Gmax','Sliders',255,255,updateGreenMax)
cv2.createTrackbar('Bmin','Sliders',0,255,updateBlueMin)
cv2.createTrackbar('Bmax','Sliders',255,255,updateBlueMax)


while True:
    status, img = cap.read()
    cv2.imshow("Video", img)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.imshow("HSV",hsv)
# define range of selected color in HSV
    lower_range = np.array([redMin,greenMin,blueMin])
    upper_range = np.array([redMax,greenMax,blueMax])
#create a mask
    mask = cv2.inRange(img,lower_range,upper_range)
    colormask = cv2.bitwise_and(img,img, mask= mask)
    cv2.imshow("Color Finder", colormask);
  
    k = cv2.waitKey(1)
    if k == 27:
        break
cv2.destroyAllWindows()
