import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Membaca gambar
img = mpimg.imread('testing.jpg')

# Menampilkan gambar
plt.imshow(img)
plt.axis('off')  # Menonaktifkan sumbu (opsional)
plt.show()