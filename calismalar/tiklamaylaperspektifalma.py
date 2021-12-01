import cv2
import numpy as np

circles = np.zeros((4, 2), np.int)  # 4-2 lik int alan bir matris oluşturduk
counter = 0  # 4 köşe alıcağımızdan bir sayac koyduk her click +1 yapacak


def mousePoints(event, x, y, flags, params):
    global counter  # counter parametresini global yaptık
    if event == cv2.EVENT_LBUTTONDOWN:  # left click fonksiyonu

        circles[counter] = x, y  # matrise her clickin x ve y sini atadık
        counter = counter + 1  # her tıklamada sayac bir artıyo
        print(circles)  # matrixe eklenen clicki direk yazdırdık


img = cv2.imread("resimler/kitap.jpg")
while True:

    if counter == 4:
        width, height = 250, 350
        # paintten aldığımız piksel değerlerini resmin üstünde tanımladık
        pts1 = np.float32([circles[0], circles[1], circles[2], circles[3]])
        pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        output = cv2.warpPerspective(img, matrix, (width, height))
        cv2.imshow("Output Image", output)

    for x in range(0, 4):
        cv2.circle(img, (circles[x][0], circles[x][1]),
                   3, (0, 255, 0), cv2.FILLED)

    cv2.imshow("Original Image", img)
    cv2.setMouseCallback("Original Image", mousePoints)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.waitKey(1)