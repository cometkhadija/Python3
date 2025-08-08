import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from scipy.ndimage import uniform_filter

img_rgb = io.imread('C:/Users/ASUS/Desktop/Python3/misc/4.1.04.tiff')

# Prepare an empty array for the filtered image
img_avg_rgb = np.zeros_like(img_rgb)

# Apply average (uniform) filter on each RGB channel separately (size=3x3)
for i in range(3):
    img_avg_rgb[:, :, i] = uniform_filter(img_rgb[:, :, i], size=3)

# Plot original and average filtered RGB images
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

axes[0].imshow(img_rgb)
axes[0].set_title('Original RGB')
axes[0].axis('off')

axes[1].imshow(img_avg_rgb.astype(np.uint8))
axes[1].set_title('Average Filtered RGB (3×3)')
axes[1].axis('off')

plt.tight_layout()
plt.show()
