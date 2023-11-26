import cv2
import numpy as np 
import matplotlib.pyplot as plt

img = cv2.imread(filename="pirincler.jpg", flags=0)
print(img.shape)
img = cv2.resize(src=img, dsize=(800,600))


ret, img_threshold = cv2.threshold(src=img, 
                        thresh=70, 
                        maxval=255,
                        type=cv2.THRESH_BINARY)
cv2.imshow(winname="threshold", mat=img_threshold)


# Etiketlemek için bir kopya oluşturuyoruz
labeled_img = np.zeros_like(img_threshold)


num_pirinc_taneleri = 0
current_label = 1  # İlk etiket 1'den başlar

for y in range(img_threshold.shape[0]):
    for x in range(img_threshold.shape[1]):
        if img_threshold[y, x] == 255 and labeled_img[y, x] == 0:
            stack = [(y, x)]
            labeled_img[y, x] = current_label
            num_pirinc_taneleri += 1

            while stack:
                current_pixel_y, current_pixel_x = stack.pop()

                for i in range(-1, 2):
                    for j in range(-1, 2):
                        new_pixel_y, new_pixel_x = current_pixel_y + i, current_pixel_x + j

                        if 0 <= new_pixel_y < img_threshold.shape[0] and 0 <= new_pixel_x < img_threshold.shape[1]:
                            if img_threshold[new_pixel_y, new_pixel_x] == 255 and labeled_img[new_pixel_y, new_pixel_x] == 0:
                                stack.append((new_pixel_y, new_pixel_x))
                                labeled_img[new_pixel_y, new_pixel_x] = current_label

            current_label += 1

print(f"Pirinç Taneleri Sayısı: {num_pirinc_taneleri}")


img = cv2.putText(img=img, 
                  text=str(num_pirinc_taneleri)+" pirinc var", 
                  org=(25,50), fontFace=cv2.FONT_HERSHEY_SIMPLEX, 
                  fontScale=1, 
                  color=(255,255,255),
                  thickness=3)


cv2.imshow(winname="img", mat=img)
cv2.waitKey()