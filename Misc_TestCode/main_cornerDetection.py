import cv2
import numpy as np
import time
import math
cap = cv2.VideoCapture(1)

while 1:
    boardcorners = []
    theoCorners = []

    res, img = cap.read()
    if res:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # img = np.float32(img)
        # dst = cv2.cornerHarris(gray, 2, 3, 0.04)
        # dst = cv2.dilate(dst, None)
        # img[dst > 0.01*dst.max()] = [0, 0, 255]

        corners = cv2.goodFeaturesToTrack(gray, 85, 0.1, 10)
        corners = np.int0(corners)
        # print corners
        # print corners.min(axis=0)[0,0]
        # print corners.min(axis=0)[0,1]
        # print "***"
        for i in corners:
            # print i
            x, y = i.ravel()
            if x == corners.min(axis=0)[0, 0] or y == corners.min(axis=0)[0, 1]:
                # print "YES"
                boardcorners.append((x, y))
                cv2.circle(img, (x, y), 3, (0, 0, 255), 1)
            elif x == corners.max(axis=0)[0, 0] or y == corners.max(axis=0)[0, 1]:
                boardcorners.append((x, y))
                cv2.circle(img, (x, y), 3, (0, 0, 255), 1)
            else:
                cv2.circle(img, (x, y), 3, 255, 1)
        boardcorners.sort()
        boardcorners[-2], boardcorners[-1] = boardcorners[-1], boardcorners[-2]
        xl1, yl1 = boardcorners[-1]
        for i in boardcorners:
            cv2.line(img, (xl1, yl1), i, (0, 255, 0), 2)
            xl1, yl1 = i


        # pts1 = np.float32(boardcorners)
        # pts2 = np.float32([[0, 0], [0, 300], [300, 300], [300, 0]])
        # M = cv2.getPerspectiveTransform(pts1, pts2)
        # dst2 = cv2.warpPerspective(img, M, (300, 300))


        # Finding the intermediate points of the 4 side.
        # for i in range(len(boardcorners)-1):
        #     # Defining the two end points of each side.
        #     x1 = boardcorners[i][0]
        #     x2 = boardcorners[i+1][0]
        #     y1 = boardcorners[i][1]
        #     y2 = boardcorners[i+1][1]
        #     # The length of the side.
        #     norm = math.sqrt((x2 - x1)**2 + (y2 - y2)**2)
        #     try:
        #         # Calculate the slope of the side.
        #         slope = float(y2 - y1) / (x2 - x1)
        #     except Exception as e:
        #         print e.message
        #     # Divide the side into 8 small lengths.
        #     side = norm / 8.0
        #     # Find the angle of the slope.
        #     angle = math.atan(slope)
        #     # For each small segment, find the x,y for the end points of it.
        #     for j in range(7):
        #         # Using an initial point (x,y) and the length and the angle, find the new endpoint (x_new, y_new).
        #         new_x = x1 + int(side * math.cos(angle))
        #         new_y = y1 + int(side * math.sin(angle))
        #         # theoCorners.append((new_x, new_y))
        #         cv2.circle(img, (new_x, new_y), 4, (255, 255, 0), -1)
        #         x1, y1 = new_x, new_y

        print boardcorners
        # time.sleep(0.5)
        # print "***************"

        cv2.imshow("chessboard", img)
        # cv2.imshow("Corners", dst2)

        if cv2.waitKey(5) & 0xff == ord('q'):
            break
cap.release()