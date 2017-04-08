import cv2
import numpy as np

img = cv2.imread("resources/chessboard_top.jpg", 0)
img = cv2.medianBlur(img, 5)

ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
c = 0
for i in contours:
    cv2.drawContours(img, [i], -1, (0, 0, 255), 3)
    c += 1

print c
cv2.imshow("image", img)
cv2.imshow("Threshold1", thresh1)
cv2.waitKey()