import cv2

img = cv2.imread("Resources/forest.jpeg")

img_grey = cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY)

cv2.imshow("Grey",img_grey)
cv2.waitKey(0)
img_grey_invert = cv2.bitwise_not(img_grey)

img_smooth = cv2.GaussianBlur(img_grey_invert,(21,21),sigmaX=0,sigmaY=0)

cv2.imshow("Smoothed",img_smooth)
cv2.waitKey(0)

def dodgev2(x,y):
    return cv2.divide(x,255-y,scale=256)

final_img = dodgev2(img_grey,img_smooth)

cv2.imshow("Final",final_img)
cv2.waitKey(0)

cv2.destroyAllWindows()