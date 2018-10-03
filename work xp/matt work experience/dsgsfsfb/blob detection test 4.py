import time
import cv2
import numpy as np
deltat = 0.8

# create video capture
cap = cv2.VideoCapture(0)
nob = 0
nol = 0
tnow = time.time()
tnob = 0

tnow = tnow + deltat
while(1):
    nol = nol + 1
    tnob = tnob + 1
    
    # read the frames
    _,frame = cap.read()

    # smooth it
    frame = cv2.blur(frame,(3,3))

    # convert to hsv and find range of colors
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    thresh = cv2.inRange(hsv,np.array((0, 80, 80)), np.array((20, 255, 255)))
    thresh2 = thresh.copy()

    # find contours in the threshold image
    f, contours,hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    # finding contour with maximum area and store it as best_cnt
    max_area = 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > max_area:
            max_area = area
            best_cnt = cnt
            nob = nob + 1

    # finding centroids of best_cnt and draw a circle there
    M = cv2.moments(best_cnt)
    cx,cy = int(M['m10']/M['m00']), int(M['m01']/M['m00'])
    cv2.circle(frame,(cx,cy),5,255,-1)

    # Show it, if key pressed is 'Esc', exit the loop
    cv2.imshow('frame',frame)
    cv2.imshow('thresh',thresh2)
    if ((0xFF & cv2.waitKey(33)) == 27):
        break
    if ( tnow <= time.time() ):
        print(nob / nol)
        tnow = time.time() + deltat
        nol = 0
        nob = 0

# Clean up everything before leaving
cv2.destroyAllWindows()
cap.release()
print "Done..."
print(nob)
print(tnob)

