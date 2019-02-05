import cv2
import numpy as np

img = cv2.imread('images/01.jpg',cv2.IMREAD_COLOR)

#capture pixel
px = img[55,55]

#modify pixel 
img[55,55] = [255,255,255]

#modify pixel
px = img[55,55]
print(px)

px = img[100:150,100:150]
print(px)

#set white pixel matrix
img[100:150,100:150] = [255,255,255]

print(img.shape)
print(img.size)
print(img.dtype)

#crop image
crop = img[37:111,107:194]
img[0:74,0:87] = crop
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
