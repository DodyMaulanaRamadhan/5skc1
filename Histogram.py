import cv2
import numpy as np
import matplotlib.pyplot as plt

# Langkah 1: Baca gambar berformat RGB
image = cv2.imread('testing.jpg')

# Check if the image was loaded correctly
if image is None:
    print("Error: Image not found or failed to load.")
else:
    # Pisahkan channel Blue, Green, Red
    B = image[:,:,0]  # Blue layer
    G = image[:,:,1]  # Green layer
    R = image[:,:,2]  # Red layer

    # Langkah 2: Hitung histogram masing-masing channel
    b_histogram = cv2.calcHist([image], [0], None, [256], [0, 256])
    g_histogram = cv2.calcHist([image], [1], None, [256], [0, 256])
    r_histogram = cv2.calcHist([image], [2], None, [256], [0, 256])

    # Langkah 3: Equalize setiap channel
    b_equi = cv2.equalizeHist(B)
    g_equi = cv2.equalizeHist(G)
    r_equi = cv2.equalizeHist(R)

    # Langkah 4: Hitung histogram setelah equalization
    b_histogramEqui = cv2.calcHist([b_equi], [0], None, [256], [0, 256])
    g_histogramEqui = cv2.calcHist([g_equi], [0], None, [256], [0, 256])
    r_histogramEqui = cv2.calcHist([r_equi], [0], None, [256], [0, 256])

    # Langkah 5: Plot histogram sebelum dan sesudah equalization
    plt.figure(figsize=(10, 8))

    # Original histograms
    plt.subplot(2, 3, 1)
    plt.plot(b_histogram, color='b')
    plt.title('Blue Channel Histogram')

    plt.subplot(2, 3, 2)
    plt.plot(g_histogram, color='g')
    plt.title('Green Channel Histogram')

    plt.subplot(2, 3, 3)
    plt.plot(r_histogram, color='r')
    plt.title('Red Channel Histogram')

    # Equalized histograms
    plt.subplot(2, 3, 4)
    plt.plot(b_histogramEqui, color='b')
    plt.title('Equalized Blue Channel Histogram')

    plt.subplot(2, 3, 5)
    plt.plot(g_histogramEqui, color='g')
    plt.title('Equalized Green Channel Histogram')

    plt.subplot(2, 3, 6)
    plt.plot(r_histogramEqui, color='r')
    plt.title('Equalized Red Channel Histogram')

    # Show the plots
    plt.tight_layout()
    plt.show()