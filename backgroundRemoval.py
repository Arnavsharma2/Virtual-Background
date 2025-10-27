import cv2 as cv
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
from cvzone.FPS import FPS
import numpy as np
import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

cap = cv.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
ss = SelfiSegmentation()
listImg = os.listdir('images')
for i in range(len(listImg)):
    listImg[i] = "images/" + listImg[i]
# print(listImg)
indexImg = 0

while True:
    print(listImg[indexImg])
    _,img = cap.read()
    imgBg = cv.imread(listImg[indexImg])
    imgBg = cv.resize(imgBg, (640, 480))
    imgOut = ss.removeBG(img, imgBg)
    cv.imshow('Image', imgOut)
    key = cv.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('a'):
        if indexImg > 0:
            indexImg -= 1
    elif key == ord('d'):
        if indexImg < len(listImg)-1:
            indexImg += 1
        
    
cap.release()
cv.destroyAllWindows()
    
    