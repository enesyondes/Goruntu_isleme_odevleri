import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def mask_process(frame):
    frame_hsv = cv2.cvtColor(src=frame, code=cv2.COLOR_BGR2HSV)
    
    # kırmızı rengi için alt ve üst sınırları alıyoruz
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    mask = cv2.inRange(src=frame_hsv, lowerb=lower_red, upperb=upper_red)

    res = cv2.bitwise_and(src1=frame, src2=frame, mask=mask)

    return mask,res

while True:
    _,frame = cap.read()
    frame = cv2.flip(src=frame, flipCode=1)
        
    mask, res = mask_process(frame)
    
    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("result", res)

    # Bekleme ve kapatma işlemleri
    if cv2.waitKey(1) and 0xFF == ord("q"):
        break

cv2.destroyAllWindows()