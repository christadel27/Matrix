import cv2
import matplotlib.pyplot as plt
import numpy as np

sample_gambar = r"C:\Users\Adelia\Downloads\photo_2023-06-19_12-46-48.jpg"
img = cv2.imread(sample_gambar)
print(img.shape)

img_yellow = img[:,:,2]  # Menggunakan saluran warna kuning (indeks 2)
plt.imshow(img_yellow)
plt.show()

red = img[:, :, 0] # Menggunakan saluran warna merah (indeks 0)
green = img[:, :, 1] # Menggunakan saluran warna hijau (indeks 1)
blue = img[:, :, 2] # Menggunakan saluran warna biru (indeks 2)
grayscale = 0.299 * red + 0.587 * green + 0.114 * blue
grayscale = grayscale.astype(np.uint8)
plt.imshow(grayscale, cmap='gray')
plt.colorbar()
plt.show()
img_bgr = cv2.imread(sample_gambar)
img = img_bgr[:,:,::-1]
red = img[:, :, 0]
green = img[:, :, 1]
blue = img[:, :, 2]
grayscale = 0.299 * red + 0.587 * green + 0.114 * blue
grayscale = grayscale.astype(np.uint8)
fig, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4, figsize=(12,4))
ax1.imshow(red, cmap='gray')
ax1.set_title('Red channel')
ax2.imshow(green, cmap='gray')
ax2.set_title('Green channel')
ax3.imshow(blue, cmap='gray')
ax3.set_title('Blue channel')
ax4.imshow(grayscale, cmap='gray')
ax4.set_title('Grayscale using formula channel')
# plt.colorbar()
plt.show()
