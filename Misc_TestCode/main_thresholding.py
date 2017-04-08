import cv2
import numpy as np

img = cv2.imread("resources/chessboard_top.jpg", 0)
img = cv2.medianBlur(img, 5)

ret, thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

cv2.imshow("image", img)
cv2.imshow("Threshold1", thresh1)
cv2.imshow("Threshold2", th2)
cv2.waitKey(0)