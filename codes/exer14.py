import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while 1:
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	template = cv2.imread('images/coin.jpg',0)
	w, h = template.shape[::-1]
	res = cv2.matchTemplate(gray,template,cv2.TM_CCOEFF_NORMED)
	threshold = 0.8
	loc = np.where( res >= threshold)
	for pt in zip(*loc[::-1]):
		cv2.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)

	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()