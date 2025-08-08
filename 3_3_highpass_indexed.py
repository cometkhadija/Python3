import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve
from skimage import io

# Load image (GIF may have multiple frames)
img = io.imread('C:/Users/ASUS/Desktop/Python3/misc/indexed_GIF.gif')

# Take only the first frame if 4D
if img.ndim == 4:
    img = img[0]

# High-pass kernel
high_pass_kernel = np.array([[0, -1, 0],
                             [-1, 4, -1],
                             [0, -1, 0]])

# Prepare output
if img.ndim == 3:
    img_high = np.zeros_like(img)
    for i in range(img.shape[2]):
        img_high[:, :, i] = convolve(img[:, :, i], high_pass_kernel)
else:
    img_high = convolve(img, high_pass_kernel)

# Plot
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
axes[0].imshow(img)
axes[0].set_title('Original Indexed')
axes[0].axis('off')

axes[1].imshow(img_high)
axes[1].set_title('High-Pass Filtered')
axes[1].axis('off')

plt.tight_layout()
plt.show()
