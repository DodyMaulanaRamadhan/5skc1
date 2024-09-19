import cv2
import numpy as np
import matplotlib.pyplot as plt

# Langkah 1: Baca gambar berwarna
image = cv2.imread('KopiTanjung.jpeg')

# Langkah 2: Translasi gambar sebesar 50 piksel ke kanan dan 30 piksel ke bawah
height, width = image.shape[:2]
translation_matrix = np.float32([[1, 0, 50], [0, 1, 30]])
translated_image = cv2.warpAffine(image, translation_matrix, (width, height))

# Langkah 3: Rotasi gambar sebesar 45 derajat searah jarum jam
center = (width // 2, height // 2)
rotation_matrix = cv2.getRotationMatrix2D(center, -45, 1)  # -45 untuk rotasi searah jarum jam
rotated_image = cv2.warpAffine(translated_image, rotation_matrix, (width, height))

# Langkah 4: Tampilkan gambar asli, hasil translasi, dan hasil rotasi secara berdampingan
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axes[0].set_title('Gambar Asli')
axes[0].axis('off')

axes[1].imshow(cv2.cvtColor(translated_image, cv2.COLOR_BGR2RGB))
axes[1].set_title('Hasil Translasi')
axes[1].axis('off')

axes[2].imshow(cv2.cvtColor(rotated_image, cv2.COLOR_BGR2RGB))
axes[2].set_title('Hasil Rotasi')
axes[2].axis('off')

plt.tight_layout()
plt.show()
