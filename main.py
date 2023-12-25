import numpy
import os
import cv2
cap= cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
imgBackground = cv2.imread('Resources/background.png')
folderPath='Resources/Modes'
modePathList=os.listdir(folderPath)
imgModeList= []
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderPath,path)))
while True:
    success, img=cap.read()
    imgBackground[162:162+480,55:55+640] = img
    imgBackground[44:44+633,808:808+414] = imgModeList[]
    #cv2.imshow("webcam" , img)
    cv2.imshow("face Attendece",imgBackground)
    cv2.waitKey(1)


