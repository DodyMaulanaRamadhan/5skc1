import matplotlib.pyplot as plt
from skimage import io, color, filters

# Langkah 1: Baca gambar berformat grayscale
image = io.imread('storage/grayscale.jpg', as_gray=True)

# Langkah 2: Terapkan Otsu's Thresholding
threshold_value = filters.threshold_otsu(image)
binary_image = image > threshold_value

# Langkah 3: Tampilkan gambar asli dan hasil thresholding berdampingan
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].imshow(image, cmap='gray')
axes[0].set_title('Gambar Asli')
axes[0].axis('off')

axes[1].imshow(binary_image, cmap='gray')
axes[1].set_title('Hasil Thresholding (Otsu)')
axes[1].axis('off')

plt.tight_layout()
plt.show()