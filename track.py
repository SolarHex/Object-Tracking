import cv2
import numpy as np

cam = cv2.VideoCapture('los_angeles.mp4')

_, frame = cam.read()
old_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

lk_params = dict(winSize = (10,10), maxlevel = 4, criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,10,0.03))

def clicks (event,x,y,flags,params):
    global point, point_selected, old_points
    if event == cv2.EVENT_LBUTTONDOWN:
        point = (x,y)
        point_selected = True  
        old_points = np.array([[x,y]], dtype = np.float32)
        
cv2.namedWindow('Traffic')
cv2.setMouseCallback('Traffic',clicks)

point_selected = False
point = ()
old_points = np.array([[]])

while True:  
    ret, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    if ret == False:  
        cam = cv2.VideoCapture('los_angeles.mp4')
        continue
    
    if point_selected is True:
        cv2.circle(frame, point, 5, (0,0,255), -1)
        
    new_points, status, error = cv2.calcOpticalFlowPyrLK(old_gray, gray, old_points, None, **lk_params)
    old_gray = gray.copy()
    
    x, y = new_points.ravel()
    cv2.circle(frame, (x,y), 5,(0,255,0),-1 )
    
    
    cv2.imshow('Traffic', frame)
    
    if cv2.waitKey(1) == ord('q'):
        break
    
cam.release()
cv2.destroyAllWindows()