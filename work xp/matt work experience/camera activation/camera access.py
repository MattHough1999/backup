import cv2
cap = cv2.VideoCapture(0)
running = True

while running:
    ret, frame = cap.read()
    cv2.imshow("show",frame)
    if ((0xFF & cv2.waitKey(100)) == 27):
        running = False
cv2.destroyAllWindows()
#cv2.destroyallwindows doesn't close the camera frame it only freezes the frame
