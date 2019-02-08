import cv2
import numpy as np

img = cv2.imread('images/book.jpg')
grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#adaptive
th = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
#simple
retval, threshold = cv2.threshold(grayscaled, 10, 255, cv2.THRESH_BINARY)
#use otsu
retval2,threshold2 = cv2.threshold(grayscaled,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('original',img)
cv2.imshow('threshold',threshold)
cv2.imshow('threshold2',threshold2)
cv2.imshow('th',th)
cv2.waitKey(0)
cv2.destroyAllWindows()