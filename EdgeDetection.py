import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Resources/Shivani.JPG")
# cv2.imshow('Original', img)
# cv2.waitKey(0)

# img_gray = cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY)
# cv2.imshow('Grey', img_gray)
# cv2.waitKey(0)

img_blur = cv2.blur(img, (3,3),0)
cv2.imshow('Blur Image', img_blur)
cv2.waitKey(0)

# edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200) # Canny Edge Detection
# cv2.imshow('Canny Edge Detection', edges)
# cv2.waitKey(0)
#
# sobelx = cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
#
# sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
#
# sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection
#
# cv2.imshow('Sobel X', sobelx)
# cv2.waitKey(0)
# cv2.imshow('Sobel Y', sobely)
# cv2.waitKey(0)
# cv2.imshow('Sobel X Y using Sobel() function', sobelxy)
# cv2.waitKey(0)


cv2.destroyAllWindows()
