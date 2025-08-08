import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from scipy.ndimage import convolve

img_rgb = io.imread('C:/Users/ASUS/Desktop/Python3/misc/4.1.04.tiff')

# Prepare an empty array for the filtered image
img_highpass_rgb = np.zeros_like(img_rgb)

# High-pass filter kernel (Laplacian)
high_pass_kernel = np.array([[0, -1, 0],
                             [-1, 4, -1],
                             [0, -1, 0]])

# Apply high-pass filter on each RGB channel separately
for i in range(3):
    img_highpass_rgb[:, :, i] = convolve(img_rgb[:, :, i], high_pass_kernel)

# Clip values to display range
img_highpass_rgb = np.clip(img_highpass_rgb, 0, 255)

fig, axes = plt.subplots(1, 2, figsize=(12, 6))

axes[0].imshow(img_rgb)
axes[0].set_title('Original RGB')
axes[0].axis('off')

axes[1].imshow(img_highpass_rgb.astype(np.uint8))
axes[1].set_title('High-pass Filtered RGB (Laplacian)')
axes[1].axis('off')

plt.tight_layout()
plt.show()
