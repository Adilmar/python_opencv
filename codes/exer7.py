import cv2
import numpy as np

img1 = cv2.imread('images/p1.png')
img2 = cv2.imread('images/p2.png')

weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)
cv2.imshow('weighted',weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()
