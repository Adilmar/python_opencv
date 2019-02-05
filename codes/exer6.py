import cv2
import numpy as np

# 500 x 250
img1 = cv2.imread('images/p1.png')
img2 = cv2.imread('images/p2.png')

add = img1+img2
#add = cv2.add(img1,img2)

cv2.imshow('add',add)
cv2.waitKey(0)
cv2.destroyAllWindows()
