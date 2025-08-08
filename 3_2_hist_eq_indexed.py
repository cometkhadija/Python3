import numpy as np
import matplotlib.pyplot as plt
from skimage import io, color, exposure, img_as_float

# Load GIF (multi-frame)
img_gif = io.imread('C:/Users/ASUS/Desktop/Python3/misc/indexed_GIF.gif')

# Take first frame only
img_rgb = img_as_float(img_gif[0])

# Convert RGB to HSV
img_hsv = color.rgb2hsv(img_rgb)

# Equalize histogram of V channel
img_hsv[:, :, 2] = exposure.equalize_hist(img_hsv[:, :, 2])

# Convert back to RGB
img_eq_rgb = color.hsv2rgb(img_hsv)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

axes[0, 0].imshow(img_rgb)
axes[0, 0].set_title("Original RGB Image (First Frame)")
axes[0, 0].axis('off')

colors = ['red', 'green', 'blue']
for i, col in enumerate(colors):
    axes[1, 0].hist(img_rgb[:, :, i].ravel(), bins=256, color=col, alpha=0.5, label=col.upper())
axes[1, 0].set_title("Histogram: Original RGB")
axes[1, 0].legend()

axes[0, 1].imshow(img_eq_rgb)
axes[0, 1].set_title("Equalized RGB (via V channel)")
axes[0, 1].axis('off')

for i, col in enumerate(colors):
    axes[1, 1].hist(img_eq_rgb[:, :, i].ravel(), bins=256, color=col, alpha=0.5, label=col.upper())
axes[1, 1].set_title("Histogram: Equalized RGB")
axes[1, 1].legend()

plt.tight_layout()
plt.show()
