import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from scipy.ndimage import uniform_filter

img = io.imread('C:/Users/ASUS/Desktop/Python3/misc/5.3.01.tiff')
img_avg = uniform_filter(img, size=3)

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
axes[0].imshow(img, cmap='gray')
axes[0].set_title('Original Grayscale')
axes[0].axis('off')

axes[1].imshow(img_avg, cmap='gray')
axes[1].set_title('Average Filtered (3×3)')
axes[1].axis('off')

plt.tight_layout()
plt.show()
