import cv2
import numpy
import os,sys

haarcascade = "haarcascade_frontalface_default.xml"

#all the faces data will be present in this folder
dataset = "images"

#a subfolder to store my face
subdata = "akshay"

path = os.path.join(dataset, subdata)
if not os.path.isdir(path):
    os.mkdir(path)

#define size of images
(width,height) = (130,100)

facecascade = cv2.CascadeClassifier(haarcascade)

#using python control webcam and take photos(use 0)
webcam = cv2.VideoCapture(0)

count = 1
while count<30:
    status,frame = webcam.read()
    greyimg = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = facecascade.detectMultiScale(greyimg)
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y), (x+w,y+h), (255,0,0), 3)
        face = greyimg[y:y + h,  x:x + w]
        face_resize =  cv2.resize(face, (width,height))
        cv2.imwrite("% s/% s.png" %(path, count), face_resize)
    count += 1
    cv2.imshow("face detection", frame)
    if cv2.waitKey(10) == 27:
        break
