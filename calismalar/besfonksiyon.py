import cv2
import numpy as np

kernel = np.ones((5, 5), np.uint8)
print(kernel)

uzunluk = 400
genislik = 400

path = "resimler/ben.jpg"
img = cv2.imread(path)
img = cv2.resize(img, (uzunluk, genislik))
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # resmi gri renge çevirmek
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)  # resmi bulanık yapma
imgCanny = cv2.Canny(imgBlur, 50, 50)  # kenar bulma fonksiyonu
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDilation, kernel, iterations=1)

cv2.imshow('benim', img)
cv2.imshow('gri ben', imgGray)
cv2.imshow('bulanik ben', imgBlur)
cv2.imshow('canny', imgCanny)
cv2.imshow("dilation", imgDilation)
cv2.imshow('eroded', imgEroded)

cv2.waitKey(0)
