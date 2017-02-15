import cv2
import numpy as np

global redMin
redMin =0
global redMax
redMax =255
global greenMin
greenMin =0
global greenMax
greenMax =255
global blueMin
blueMin =0
global blueMax
blueMax =255

def updateRedMin(x):
    print(x)
    redMin = x
def updateRedMax(x):
    redMax = x
def updateGreenMin(x):
    greenMin = x
def updateGreenMax(x):
    greenMax = x
def updateBlueMin(x):
    blueMin = x
def updateBlueMax(x):
    blueMax = x

cap = cv2.VideoCapture(0)
cv2.namedWindow("Video")
cv2.namedWindow("Sliders")
cv2.namedWindow("HSV")
cv2.namedWindow("Color Finder")

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
    lower_range = np.array([blueMin,greenMin,redMin])
    upper_range = np.array([blueMax,greenMax,redMax])
#create a mask
    mask = cv2.inRange(hsv,lower_range,upper_range)
    font = cv2.FONT_HERSHEY_SIMPLEX
    print(redMin)
  
    k = cv2.waitKey(1)
    if k == 27:
        break
cv2.destroyAllWindows()
