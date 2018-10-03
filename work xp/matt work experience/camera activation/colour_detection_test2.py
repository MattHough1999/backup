import time
import cv2
import numpy as np
import Queue
import threading

class colour_detection (threading.Thread):
    def __init__(self, frame, windowname):
        super(colour_detection, self).__init__()
        self.windowname = windowname
        self.frame = frame
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        self.YELLOW_MIN = np.array([20, 125, 125],np.uint8)
        self.YELLOW_MAX = np.array([30, 255, 255],np.uint8)
        self.RED_MIN = np.array([0, 0, 125],np.uint8)
        self.RED_MAX = np.array([75, 75, 255],np.uint8)
        self.WHITE_MIN = np.array([155, 155, 155],np.uint8)
        self.WHITE_MAX = np.array([255, 255, 255],np.uint8)
        self.GREEN_MIN = np.array([0,95, 0],np.uint8)
        self.GREEN_MAX = np.array([80, 255, 80],np.uint8)
        self.BLUE_MIN = np.array([75, 70, 0],np.uint8)
        self.BLUE_MAX = np.array([255, 190, 40],np.uint8)
        self.ORANGE_MIN = np.array([20, 125, 125],np.uint8)
        self.ORANGE_MAX = np.array([30, 255, 255],np.uint8)
        

        self.yellow = (0,255,255)
        self.orange = (0,160,255)
        self.red = (0,0,255)
        self.white = (125,125,125)
        self.green = (40,200,40)
        self.blue = (255,255,0)

    def DrawContors(self, colour_thresh, outlineColour):
        ret,thresh = cv2.threshold(colour_thresh,127,255,0)
        cv2.imshow('fred', thresh)
   
        f, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
##    print type(contours)
        for cnt in contours:
            x,y,w,h = cv2.boundingRect(cnt)
##        print x,
##        print y
            cv2.rectangle(self.im,(x,y),(x+w,y+h),outlineColour,2)

    def run(self):
        self.im = cv2.bilateralFilter(self.frame,9,75,75)
##        ntime = time.time()
##        print('bilateral filter took', ntime - stime)
        self.im = cv2.fastNlMeansDenoisingColored(self.im,None,10,10,7,21)
##        antime = time.time()
##        print('this stuff took', antime - ntime)
           # HSV image
##        anotime = time.time()
##        print('this other stuff took', anotime - antime)
        
##    cv2.imwrite('hsv_img.png', hsv_img)

        yellow_thresh = cv2.inRange(self.im, self.YELLOW_MIN, self.YELLOW_MAX)
        red_thresh = cv2.inRange(self.im, self.RED_MIN, self.RED_MAX)# Thresholding image
        white_thresh = cv2.inRange(self.im, self.WHITE_MIN, self.WHITE_MAX)
        green_thresh = cv2.inRange(self.im, self.GREEN_MIN, self.GREEN_MAX)
        blue_thresh = cv2.inRange(self.im, self.BLUE_MIN, self.BLUE_MAX)
        orange_thresh = cv2.inRange(self.im, self.ORANGE_MIN, self.ORANGE_MAX)

        self.DrawContors(yellow_thresh, self.yellow)# Thresholding image
        self.DrawContors(red_thresh, self.red)
        self.DrawContors(white_thresh, self.white)
        self.DrawContors(green_thresh, self.green)
        self.DrawContors(blue_thresh, self.blue)
        self.DrawContors(orange_thresh, self.orange)
            
        cv2.imshow(self.windowname,self.im)


cap = cv2.VideoCapture(0)

while(1):
    froicoord = (450, 80)
    sroicoord = (170, 390)
    cube_outline = (0,0,0)
    f, frame = cap.read()
    cv2.rectangle(frame, froicoord, sroicoord, cube_outline,(3), 8, (0))
    cv2.imshow('video', frame)
    ch = 0xFF & cv2.waitKey(1)
    if ch == ord('y'):
        thread = colour_detection(frame, 'colour window')
        cv2.imwrite("colourTest.jpg", frame)
        thread.start()
cap.release()
