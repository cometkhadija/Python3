import numpy as np
import matplotlib.pyplot as plt
from skimage import io, color, exposure

# Load one image
img_path = 'C:/Users/Asus/Desktop/358/DIP/Dataset/4.1.02.tiff'
img_rgb = io.imread(img_path)

# Extract R, G, B channels
r = img_rgb[:, :, 0]
g = img_rgb[:, :, 1]
b = img_rgb[:, :, 2]

# Convert to HSV
img_hsv = color.rgb2hsv(img_rgb)

# Equalize the Value (V) channel instead of Saturation (S)
img_hsv[:, :, 2] = exposure.equalize_hist(img_hsv[:, :, 2])

# Convert back to RGB
img_eq_rgb = color.hsv2rgb(img_hsv)

# Store all output images in a list
output_images = [
    ('Original RGB', img_rgb),
    ('Red Channel', r),
    ('Green Channel', g),
    ('Blue Channel', b),
    ('Equalized RGB (V-channel)', img_eq_rgb)
]

fig, axes = plt.subplots(2, 5, figsize=(20, 8))

for i, (title, img) in enumerate(output_images):
    # Show image (top row)
    ax_img = axes[0, i]
    if img.ndim == 2:
        ax_img.imshow(img, cmap='gray')
    else:
        ax_img.imshow(img)
    ax_img.set_title(title)
    ax_img.axis('off')

    # Show histogram (bottom row)
    ax_hist = axes[1, i]
    ax_hist.clear()
    if img.ndim == 2:
        # Single channel histogram
        ax_hist.hist(img.ravel(), bins=256, color='gray')
        ax_hist.set_title(f'{title} Histogram')
    else:
        # RGB histogram
        colors = ['Red', 'Green', 'Blue']
        for j, col in enumerate(colors):
            ax_hist.hist(img[:, :, j].ravel(), bins=256, color=col.lower(), alpha=0.7, label=col)
        ax_hist.set_title(f'{title} RGB Histogram')
        ax_hist.legend(fontsize='small')

plt.tight_layout()
plt.show()
