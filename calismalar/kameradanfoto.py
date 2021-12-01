import cv2
import numpy as np

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
ret, frame = cap.read()
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
cv2.imwrite('resimler/kopya.jpg',gray)
cv2.imshow('frame',gray)

cv2.waitKey(0)