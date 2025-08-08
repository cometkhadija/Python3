import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from scipy.ndimage import gaussian_filter

# Load image (RGB)
img_rgb = io.imread('C:/Users/ASUS/Desktop/Python3/misc/4.1.04.tiff')

# Prepare an empty array for the filtered image
img_gaussian_rgb = np.zeros_like(img_rgb)

# Apply Gaussian filter on each RGB channel separately (sigma=1)
for i in range(3):
    img_gaussian_rgb[:, :, i] = gaussian_filter(img_rgb[:, :, i], sigma=3)

# Plot original and Gaussian filtered RGB images
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

axes[0].imshow(img_rgb)
axes[0].set_title('Original RGB')
axes[0].axis('off')

axes[1].imshow(img_gaussian_rgb.astype(np.uint8))
axes[1].set_title('Gaussian Filtered RGB (sigma=3)')
axes[1].axis('off')

plt.tight_layout()
plt.show()
