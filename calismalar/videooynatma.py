import cv2

frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture('video/video.avi')

while True: # her bir frame görebilmemiz için bi döngü oluşturmamız lazım. döngüde sırayla frameleri görebilmemiz için
    success, img = cap.read() #sucess burada (0)indeks img(1). Başarısızsa 0 indeks çalışır başarılıysa 1 indeks çalışır. cap.read() frame frame kayıt eder
    img = cv2.resize(img, (frameWidth, frameHeight))
    cv2.imshow('Video',img) 
    

    
    if cv2.waitKey(1) & 0xFF == ord('q'): # cv2.wait() içine 1 yazarsak 1.indeksi gösterir yani döngülü frame,0 yazarsak başarısız yani tek 1 frame
         break

    
