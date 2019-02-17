import cv2
import numpy as np

img_rgb = cv2.imread('images/coins.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

#define teplate - shape
template = cv2.imread('images/coin.jpg',0)
w, h = template.shape[::-1]

#alg match 
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)

#draw rectangle if match
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)

cv2.imshow('Detected',img_rgb)
