import cv2
import numpy
import dlib


import face_recognition

img=face_recognition.load_image_file("kv.jpg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2BGRA)
face=face_recognition.face_landmarks(img)

#img=cv2.haveImageReader('kv.jpg')
#img1=cv2.imread('kv.jpg')




cv2.imshow(winname='KARTIKEYA',mat=img)
cv2.waitKey(0)
