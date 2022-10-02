import cv2
import numpy as np
from object_detection import ObjectDetection

cam = cv2.VideoCapture('los_angeles.mp4')
od = ObjectDetection()


while True:  
    ret, frame = cam.read()
    
    if not ret:
        cam = cv2.VideoCapture('los_angeles.mp4')
        continue
    
    cv2.imshow('road', frame)
    (class_ids,scores,box) = od.detect(frame)
    
    for i in box:
        (x,y,w,h) = i
        cv2.rectangle(frame, (x,y),(x+w,y+h), (255,0,0),thickness=3)
    
    
    
    
    
    if cv2.waitKey(1) == ord('q'):
        break
    
cam.release()
cv2.destroyAllWindows()