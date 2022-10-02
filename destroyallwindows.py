import cv2
import numpy as np

cam = cv2.VideoCapture(0)

def select_roma(event,x,y,flags,params):
    global point, selected_point
    if event == cv2.EVENT_LBUTTONDOWN:
        point = (x,y)      
        selected_point = True


cv2.namedWindow('road')
cv2.setMouseCallback('road', select_roma)
selected_point = False
point = ()

while True:  
    _, frame = cam.read()
    
    cv2.imshow('road', frame)
    
    if selected_point is True:  
        cv2.circle(frame, point, 5,(0,255,0),2)
    
    if cv2.waitKey(1) == ord('q'):
        break
    
cam.release()
cv2.destroyAllWindows()