import cv2
import numpy as np
import serial

ser = serial.Serial('/dev/ttyUSB0' , 9600, timeout=100)

# Kırmızı sinyali üretmek için fonksiyon
defs produce_red_signal():
    print("kırmızı")
    ser.write(b'kirmizi\n')

# Sarı sinyali üretmek için fonkiyon
def produce_yellow_signal():
    print("sarı")
    ser.write(b'sari\n')

# Yeşil sinyali üretmek için fonksiyon
def produce_green_signal():
    print("yeşil")
    ser.write(b'yesil\n')

# Video akışını başlat
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Görüntüyü BGR'den HSV'ye dönüştür
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Kırmızı rengin HSV aralığını belirle
    lower_red = np.array([161,155,84])
    upper_red = np.array([179,255, 255])
    # Kırmızı rengi içeren maskeyi oluştur
    red_mask = cv2.inRange(hsv, lower_red, upper_red)

    # Sarı rengin HSV aralığını belirle
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])
    # Sarı rengi içeren maskeyi oluştur
    yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    # Yeşil rengin HSV aralığını belirle
    lower_green = np.array([40, 100, 100])
    upper_green = np.array([70, 255, 255])
    # Yeşil rengi içeren maskeyi oluştur
    green_mask = cv2.inRange(hsv, lower_green, upper_green)

    # Tüm maskeleri birleştir
    combined_mask = red_mask + yellow_mask + green_mask

    # Gürültüyü azaltmak için morfolojik işlemler uygula
    kernel = np.ones((5, 5), np.uint8)
    combined_mask = cv2.morphologyEx(combined_mask, cv2.MORPH_OPEN, kernel)
    combined_mask = cv2.morphologyEx(combined_mask, cv2.MORPH_CLOSE, kernel)

    # Maske üzerindeki konturları bul
    contours, _ = cv2.findContours(combined_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Her bir kontur için çerçeve çiz
    for contour in contours:
        # Kontur alanını hesapla
        area = cv2.contourArea(contour)

        # Alanı kontrol et ve eğer alan belirli bir değerin üzerindeyse çerçeve çiz
        if area > 500:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
            # Konturun rengine göre uygun sinyali üret
            if np.any(red_mask[y:y+h, x:x+w]):
                produce_red_signal()
            elif np.any(yellow_mask[y:y+h, x:x+w]):
                produce_yellow_signal()
            elif np.any(green_mask[y:y+h, x:x+w]):
                produce_green_signal()

    #görüntüyü göster
    cv2.imshow('Frame', frame)
    # Çıkış için 'q' tuşuna basıldığında döngüyü kır
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Kaynakları serbest bırak
cap.release()
cv2.destroyAllWindows()