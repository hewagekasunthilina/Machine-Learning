import cv2

camera=cv2.VideoCapture(0) #0 for default camera

face_clsfr=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_clfsfr=cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

while(True):
    
    ret,img=camera.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces=face_clsfr.detectMultiScale(gray)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    
    cv2.imshow('LIVE',img)
    cv2.waitKey(10)  #10 miliseconds
