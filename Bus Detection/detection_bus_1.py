# -*- coding: utf-8 -*-

import cv2
cascade_src = 'Bus_front.xml'
video_src = 'bus1.mp4'


cap = cv2.VideoCapture(video_src)

bus_cascade = cv2.CascadeClassifier(cascade_src)

while True:
    ret, img = cap.read()
    
    if (type(img) == type(None)):
        break
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    bus = bus_cascade.detectMultiScale(gray, 1.16, 1)
    ret, thresh = cv2.threshold(gray, 127, 255, 0)
    cnts, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    QttyOfContours = 0
    for (x,y,w,h) in bus:
        QttyOfContours = QttyOfContours+1
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)   
        CoordXCentroid = int((x+x+w)/2)
        CoordYCentroid = int((y+y+h)/2)
        ObjectCentroid = (CoordXCentroid,CoordYCentroid)
        cv2.circle(img, ObjectCentroid, 1, (0, 0, 0), 5)
    print ("Total countours found: " , str(QttyOfContours))
    
    cv2.imshow('video', img)
    
    if cv2.waitKey(33) == 27:
        break
cv2.destroyAllWindows()
