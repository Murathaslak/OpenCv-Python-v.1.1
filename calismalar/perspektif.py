import cv2
import numpy as np

img = cv2.imread("resimler/kitap.jpg")

width, height = 250, 350
pts1 = np.float32([[114, 57], [232, 47], [173, 197], [334, 164]])
# paintten aldığımız piksel değerlerini resmin üstünde tanımladık
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
output = cv2.warpPerspective(img, matrix, (width, height))

for x in range(0, 4):
    # çember fonksiyonuyla tanımlı piksellere çember attık
    cv2.circle(img, (pts1[x][0], pts1[x][1]), 5, (0, 0, 255), cv2.FILLED)


cv2.imshow("Original Image", img)
cv2.imshow("Output Image", output)

cv2.waitKey(0)


# sol üss 114,57
# sağ üst 232,47
# sol alt 173,197
# sağ alt 334,164
