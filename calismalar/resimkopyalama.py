import cv2
import numpy as np

img = cv2.imread('ben.jpg',0)
cv2.imshow('image',img)

k=cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('kopya.jpg',img)
    cv2.destroyAllWindows()