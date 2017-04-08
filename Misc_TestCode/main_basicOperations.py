import cv2
import numpy as np

im1 = cv2.imread("resources/kyoto-wallpaper.jpg")
im2 = cv2.imread("resources/kyoto-wallpaper2.jpg")

dest = cv2.addWeighted(im1,0.3, im2, 0.7, 0)
gray = cv2.cvtColor(im1,cv2.COLOR_BGR2GRAY)
print im1.shape, gray.shape
print im1.size, gray.size
print im1.dtype, gray.dtype

cv2.imshow("image with no red", dest)
cv2.waitKey(0)