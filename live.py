import cv2

camera=cv2.VideoCapture(0) #0 for default camera

while(True):
    ret,img=camera.read()
    cv2.imshow('LIVE',img)
    cv2.waitKey(10)  #10 miliseconds
