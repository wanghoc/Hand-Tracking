import cv2
from cvzone.HandTrackingModule import HandDetector
import socket

#Parameters
width, height = 1280,720

#Webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4,720)

#Hand Detector
detector = HandDetector(maxHands=1, detectionCon=0.8)

#Communication
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
severAddressPort = ("127.0.0.1",5052)

while True:
    #Get the frame from the webcam
    success, img = cap.read()
    #hands
    hands,img = detector.findHands(img)

    data=[]
    #landmark values - (x,y,z)*21
    if hands:
        #get the first hand detected
        hand = hands[0]
        #get the landmark list
        lmList = hand['lmList']
        # print(lmList)
        for lm in lmList:
            data.extend([lm[0], height - lm[1],lm[2]])
            # print(data)
            sock.sendto(str.encode(str(data)),severAddressPort)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
