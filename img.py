import cv2

img=cv2.imread('Samples/flower.jpg')

cv2.rectangle(img,(40,40),(140,140),(0,255,0),5)

cv2.putText(img,'Rectangle1',(40,40),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255),2)
cv2.imshow('FLOWER',img)
