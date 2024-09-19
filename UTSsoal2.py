import cv2
import matplotlib.pyplot as plt

# Langkah 1: Baca gambar dalam format grayscale
image = cv2.imread('storage/grayscale.jpg', cv2.IMREAD_GRAYSCALE)

# Langkah 2: Terapkan Gaussian Blur untuk mengurangi noise
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

# Langkah 3: Deteksi tepi menggunakan Canny Edge Detection
edges = cv2.Canny(blurred_image, threshold1=100, threshold2=200)

# Langkah 4: Tampilkan hasil deteksi tepi
plt.figure(figsize=(10, 5))
plt.imshow(edges, cmap='gray')
plt.title('Hasil Deteksi Tepi Menggunakan Canny')
plt.axis('off')
plt.show()
