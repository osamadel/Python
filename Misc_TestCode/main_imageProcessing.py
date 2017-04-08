import cv2
import numpy as np

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print "Was Not Opened."
    cap.open()
    print "Now is Open."

while True:

    ret, frame = cap.read()
    if ret:
        # Convert the frame to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # define the ranges of blue color in HSV
        lower_blue = np.array([100, 50, 50])
        upper_blue = np.array([140, 255, 255])

        # Threshold the HSV image to get the blue objects
        mask = cv2.inRange(hsv, lower_blue, upper_blue)

        # Bitwise-AND mask and the original image
        res = cv2.bitwise_and(frame, frame, mask=mask)

        cv2.imshow("frame", frame)
        cv2.imshow("mask", mask)
        cv2.imshow("res", res)

        k = cv2.waitKey(5) & 0xff
        if k == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()