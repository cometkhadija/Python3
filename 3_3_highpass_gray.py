import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from scipy.ndimage import convolve

img = io.imread('C:/Users/ASUS/Desktop/Python3/misc/5.3.01.tiff')
high_pass_kernel = np.array([[0, -1, 0],
                             [-1, 4, -1],
                             [0, -1, 0]])
img_high = convolve(img, high_pass_kernel)

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
axes[0].imshow(img, cmap='gray')
axes[0].set_title('Original Grayscale')
axes[0].axis('off')

axes[1].imshow(img_high, cmap='gray')
axes[1].set_title('High-Pass Filtered')
axes[1].axis('off')

plt.tight_layout()
plt.show()
