import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from scipy.ndimage import gaussian_filter

img = io.imread('C:/Users/ASUS/Desktop/Python3/misc/5.3.01.tiff')
img_gaussian = gaussian_filter(img, sigma=3)

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
axes[0].imshow(img, cmap='gray')
axes[0].set_title('Original Grayscale')
axes[0].axis('off')

axes[1].imshow(img_gaussian, cmap='gray')
axes[1].set_title('Gaussian Filtered (σ=3)')
axes[1].axis('off')

plt.tight_layout()
plt.show()
