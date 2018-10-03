import numpy as np
import cv2
import time
# create video capture
cap = cv2.VideoCapture(0)
YELLOW_MIN = np.array([20, 125, 125],np.uint8)       # HSV color code lower and upper bounds
YELLOW_MAX = np.array([30, 255, 255],np.uint8)

BLUE_MIN = np.array([85, 45 ,50])
BLUE_MAX = np.array([255, 0 ,0])

ret, im = cap.read()
cv2.imshow("Show",im)

processing = True
while(processing):
    
    pready = True
    print('press space for the next image')
    c = 0
    while pready:
        ch = cv2.waitKey(1) & 0xFF

        c = c + 1
        print(ch, pready)
        if ch == ord(' '):
            pready = False
        if ch == 27:
            processing = False
            pready = False
        if c > 1000:
            processing = False
            pready = False

    if processing :        
        print('next image')
        stime = time.time()
        ret, im = cap.read()
        im = cv2.bilateralFilter(im,9,75,75)
        ntime = time.time()
        print('bilateral filter took', ntime - stime)
##        im = cv2.fastNlMeansDenoisingColored(im,None,10,10,7,21)
        antime = time.time()
        print('this stuff took', antime - ntime)
##        hsv_img = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)   # HSV image
        anotime = time.time()
        print('this other stuff took', anotime - antime)
        
##    cv2.imwrite('hsv_img.png', hsv_img)

        frame_threshed = cv2.inRange(im, YELLOW_MIN, YELLOW_MAX)     # Thresholding image
        imgray = frame_threshed
        ret,thresh = cv2.threshold(frame_threshed,127,255,0)
        f, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
##    print type(contours)
        for cnt in contours:
            x,y,w,h = cv2.boundingRect(cnt)
##        print x,
##        print y
            cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
            
        cv2.imshow("Show",im)
            
    
##cv2.imwrite("extracted.jpg", im)
##cv2.waitKey()
cv2.destroyAllWindows()
