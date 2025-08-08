import numpy as np
import matplotlib.pyplot as plt
from skimage import io, exposure, img_as_float

# Load grayscale image as float
img_gray = img_as_float(io.imread('C:/Users/ASUS/Desktop/Python3/misc/5.3.01.tiff'))

# Histogram equalization
img_eq = exposure.equalize_hist(img_gray)

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

axes[0, 0].imshow(img_gray, cmap='gray')
axes[0, 0].set_title("Original Grayscale Image")
axes[0, 0].axis('off')

axes[1, 0].hist(img_gray.ravel(), bins=256, color='black')
axes[1, 0].set_title("Histogram: Original Grayscale")

axes[0, 1].imshow(img_eq, cmap='gray')
axes[0, 1].set_title("Equalized Grayscale Image")
axes[0, 1].axis('off')

axes[1, 1].hist(img_eq.ravel(), bins=256, color='black')
axes[1, 1].set_title("Histogram: Equalized Grayscale")

plt.tight_layout()
plt.show()
