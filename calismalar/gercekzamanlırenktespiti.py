import cv2
import numpy as np
from numpy.core.shape_base import hstack


frameWidth = 600
frameHeight = 600
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)


def empty(a):
    pass


cv2.namedWindow("HSV")
cv2.resizeWindow("HSV", 640, 240)
# normalde 0-360 kadar renk değeri var ama opencv de 0-180 kadar doygunluk 255 e kadar
# renk-doygunluk-parlaklık hsv renk uzayı
cv2.createTrackbar("HUE Min", "HSV", 0, 179, empty)
cv2.createTrackbar("HUE Max", "HSV", 179, 179, empty)
cv2.createTrackbar("Sat Min", "HSV", 0, 255, empty)
cv2.createTrackbar("Sat Max", "HSV", 255, 255, empty)
cv2.createTrackbar("Value Min", "HSV", 0, 255, empty)
cv2.createTrackbar("Value Max", "HSV", 255, 255, empty)

while True:

    _, img = cap.read()
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("HUE Min", "HSV")
    h_max = cv2.getTrackbarPos("HUE Max", "HSV")
    s_min = cv2.getTrackbarPos("Sat Min", "HSV")
    s_max = cv2.getTrackbarPos("Sat Max", "HSV")
    v_min = cv2.getTrackbarPos("Value Min", "HSV")
    v_max = cv2.getTrackbarPos("Value Max", "HSV")

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    # ayarlanan değerlere göre threshold uygula
    mask = cv2.inRange(imgHsv, lower, upper)
    # maskeyi ana resme işliyoruz
    result = cv2.bitwise_and(img, img, mask=mask)

    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    hStack = np.hstack([img, mask, result])

    #cv2.imshow('Result', result)
    #cv2.imshow('Mask', mask)
    #cv2.imshow('Original', img)
    #cv2.imshow('imgHsv', imgHsv)
    cv2.imshow('hStack', hStack)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cap.destroyAllWindows()


# Hsv renkleri rgb bgr renklerine göre daha doygun ve canlı görünüyor o yüzden hsv çeviriyoruz
# Bu yüzden renklerimizi hsv den alacağız ama renk değerlerini bilmiyoruz
# 3 değişkenimiz var minimum renk tonu maximum renk tonu ve doygunluk
# bu yüzden istenen sonucu elde edene kadar oynarak bulmamız gerekiyor
# ama bunun için opencv de izleme çubuğuyla kolayca ayarlayabiliriz
# bu yüzden izleme çubuğu ekleyeceğiz

