import numpy as np
import cv2
from PIL import Image, ExifTags
# capture video
cap = cv2.VideoCapture('cabc30fc-e7726578.mov')
#descripe a loop
#read video frame by frame
while True:
    ret,image = cap.read()
    cv2.imshow('Original Video',image)
    #flip for truning(fliping) frames of video
    #img2=cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)
    try:
    
        for orientation in ExifTags.TAGS.keys():
                if ExifTags.TAGS[orientation]=='Orientation':
                    break

                exif=dict(image._getexif().items())

                if exif[orientation] == 3:
                    image = cv2.flip(image,-1)
                elif exif[orientation] == 6:
                    image=cv2.rotate(image,cv2.ROTATE_90_COUNTERCLOCKWISE)
                elif exif[orientation] == 8:
                    image=cv2.rotate(image,cv2.ROTATE_90_CLOCKWISE)
                
    except (AttributeError, KeyError, IndexError):
        # cases: image don't have getexif
        pass
    cv2.imshow('Flipped video',image)
    k=cv2.waitKey(30) & 0xff
    #once you inter Esc capturing will stop
    if k==27:
        break
cap.release()
cv2.destroyAllWindows()