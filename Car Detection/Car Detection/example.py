import cv2
import matplotlib.pyplot as plt
from cvlib.cvlib.object_detection import draw_bbox
from cvlib.cvlib.object_detection import detect_common_objects
video_src = '01.10900.wmv'

cap = cv2.VideoCapture(video_src)
frameBck = cv2.createBackgroundSubtractorMOG2(detectShadows=True)

while True:
    ret, frame1 = cap.read()
    if (type(frame1) == type(None)):
        break
    fgMask = frameBck.apply(frame1)
    contornosimg = fgMask.copy()
    im, contornos, hierarchy = cv2.findContours(contornosimg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for c in contornos:

        if cv2.contourArea(c) < 200:
            continue
    if area>area2:
        m=cv2.moments(c)

        cx=int(m['m10']/m['m00'])
        cy=int(m['m01']/m['m00'])            
        (x, y, w, h) = cv2.boundingRect(c)
    cv2.imshow('video', output_image)
   
    
    if cv2.waitKey(33) == 27:
        break
cv2.destroyAllWindows()