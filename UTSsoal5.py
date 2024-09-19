import cv2
import numpy as np
import matplotlib.pyplot as plt

# Langkah 1: Baca gambar berformat grayscale
image = cv2.imread('storage/grayscale.jpg', cv2.IMREAD_GRAYSCALE)

# Langkah 2: Hitung histogram intensitas
hist_original = cv2.calcHist([image], [0], None, [256], [0, 256])

# Langkah 3: Terapkan equalisasi histogram
equalized_image = cv2.equalizeHist(image)

# Hitung histogram intensitas setelah equalisasi
hist_equalized = cv2.calcHist([equalized_image], [0], None, [256], [0, 256])

# Langkah 4: Tampilkan gambar asli dan hasil equalisasi histogram
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# Gambar asli
axes[0, 0].imshow(image, cmap='gray')
axes[0, 0].set_title('Gambar Asli')
axes[0, 0].axis('off')

# Histogram gambar asli
axes[0, 1].plot(hist_original, color='black')
axes[0, 1].set_title('Histogram Gambar Asli')
axes[0, 1].set_xlim([0, 256])

# Gambar hasil equalisasi
axes[1, 0].imshow(equalized_image, cmap='gray')
axes[1, 0].set_title('Gambar Hasil Equalisasi')
axes[1, 0].axis('off')

# Histogram gambar hasil equalisasi
axes[1, 1].plot(hist_equalized, color='black')
axes[1, 1].set_title('Histogram Hasil Equalisasi')
axes[1, 1].set_xlim([0, 256])

plt.tight_layout()
plt.show()
