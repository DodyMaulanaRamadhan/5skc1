import cv2
import numpy as np
import matplotlib.pyplot as plt

# Langkah 1: Baca gambar berformat grayscale
image = cv2.imread('storage/grayscale.jpg', cv2.IMREAD_GRAYSCALE)

# Terapkan thresholding untuk membuat gambar biner
_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Langkah 2: Terapkan operasi erosi
kernel = np.ones((5, 5), np.uint8)  # Kernel 5x5 untuk operasi morfologi
eroded_image = cv2.erode(binary_image, kernel, iterations=1)

# Terapkan operasi dilasi
dilated_image = cv2.dilate(binary_image, kernel, iterations=1)

# Langkah 3: Tampilkan gambar asli, hasil erosi, dan hasil dilasi secara berdampingan
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].imshow(binary_image, cmap='gray')
axes[0].set_title('Gambar Biner Asli')
axes[0].axis('off')

axes[1].imshow(eroded_image, cmap='gray')
axes[1].set_title('Hasil Erosi')
axes[1].axis('off')

axes[2].imshow(dilated_image, cmap='gray')
axes[2].set_title('Hasil Dilasi')
axes[2].axis('off')

plt.tight_layout()
plt.show()
