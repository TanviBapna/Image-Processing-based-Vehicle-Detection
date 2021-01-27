# -*- coding: utf-8 -*-

import cv2 
import cvlib as cv
from cvlib.cvlib.object_detection import draw_bbox
MinCountourArea = 1500  #Adjust ths value according to your usage

cascade_src = 'cars.xml'

video_src = '01.10900.wmv'

cap = cv2.VideoCapture(video_src)

car_cascade = cv2.CascadeClassifier(cascade_src)


while True:
    ret, image = cap.read()
    if (type(image) == type(None)):
        break
    imgray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(imgray, 1.1, 2)
    ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    cnts, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    QttyOfContours = 0
    for c in cnts:
        #if a contour has small area, it'll be ignored
        if cv2.contourArea(c) < MinCountourArea:
            continue
        QttyOfContours = QttyOfContours+1    
        #draw an rectangle "around" the object
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 225), 2)
        #find object's centroid
        CoordXCentroid = int((x+x+w)/2)
        CoordYCentroid = int((y+y+h)/2)
        ObjectCentroid = (CoordXCentroid,CoordYCentroid)
        cv2.circle(image, ObjectCentroid, 1, (0, 0, 0), 5)
    print ("Total countours found: " , str(QttyOfContours))
    # bbox, label, conf = cv.detect_common_objects(image)
    # output_image = draw_bbox(im, bbox, label, conf)
    cv2.imshow('video', image)
   
    
    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()
