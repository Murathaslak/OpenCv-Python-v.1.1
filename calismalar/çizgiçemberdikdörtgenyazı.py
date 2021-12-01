import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
# 512/512 matris 3 kanallı matrisin her değeri 8bitlik olacak(alacağımız değerler 0-255 arası yani 8bit)
print(img)

# (img[:] = 255, 0, 0) matrisi komple mavi yapar BGR FORMAT

cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 2)
# çizgi çekme fonksiyonu 1.başlangıc 2.bitiş 3.bgr renkleri 4. çizgi kalınlığı

cv2.rectangle(img, (350, 100), (450, 200), (0, 0, 255), cv2.FILLED)
# dikdörtgen fonksiyonu 1.başlangıc 2.bitiş 3.renkler 4.kalınlık

cv2.circle(img, (150, 400), 50, (255, 0, 0), 3)
# çember fonksiyonu 1.merkez 2.yarıcap 3.renk 4.kalınlık

cv2.putText(img, "Yazi yazma denemesi", (75, 50),
            cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 1)
# yazı yazma fonksiyonu 1.text 2.başlangıc noktası 3.yazı tipi 4.büyüklük 5.renk 6.kalınlık

cv2.imshow("img", img)
cv2.waitKey(0)
