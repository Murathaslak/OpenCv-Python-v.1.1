import cv2

path = "resimler/ben.jpg"
img = cv2.imread(path)
print(img.shape)  # resmimizin boyutlarını gösterir.

width, height = 1000, 1000
imgResize = cv2.resize(img, (width, height))  # görüntüyü yeniden boyutlama
print(imgResize.shape)

imgCropped = img[300:602, 0:602]  # görüntüyü kırpma
imgCropResize = cv2.resize(imgCropped, (img.shape[1], img.shape[0]))


cv2.imshow("resim", img)
cv2.imshow("resim boyutlaması", imgResize)
cv2.imshow("kırpılmış", imgCropped)
cv2.imshow("kırpılanı boyutlandırma", imgCropResize)
cv2.waitKey(0)
