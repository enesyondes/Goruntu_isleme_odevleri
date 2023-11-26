import cv2
import numpy as np
import matplotlib.pyplot as plt

# Resmi yükle
image_path = 'img.jpg'
image = cv2.imread(image_path)

B = image[:,:,0]
G = image[:,:,1]
R = image[:,:,2]

image = 0.2989 * R + 0.5870 * G + 0.1140 * B

# Histogram hesaplama fonksiyonu (kendi yazacağımız)
def compute_histogram(image):
    histogram = np.zeros(256, dtype=int)
    rows, cols = image.shape

    for i in range(rows):
        for j in range(cols):
            pixel_value = int(image[i, j])  # Ondalık sayıyı tam sayıya dönüştür
            histogram[pixel_value] += 1

    return histogram

# Histogramı hesapla
histogram = compute_histogram(image)

# Resmi görselleştirelim
plt.figure()
plt.imshow(image, cmap='gray')

# Histogramı görselleştirelim
plt.figure()
plt.bar(range(256), histogram, width=1)
plt.xlabel('Piksel Değeri')
plt.ylabel('Piksel Sayısı')
plt.title('Histogram')
plt.show()
