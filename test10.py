import numpy as np
import matplotlib.pyplot as plt

img1 = plt.imread('C:/Users/CSELAB-2/Desktop/Python3/misc/4.1.03.tiff')

r = img1[:, :, 0]
g = img1[:, :, 1]
b = img1[:, :, 2]

plt.figure(figsize=(10, 8))
plt.subplot(2, 2, 1)
plt.title('Original Image')
plt.imshow(img1)

hist_r, bins_r = np.histogram(r.ravel(), bins=256, range=(0, 256))
plt.subplot(2, 2, 2)
plt.title('Red Histogram')
plt.bar(bins_r[:-1], hist_r, color='red', width=1)

hist_g, bins_g = np.histogram(g.ravel(), bins=256, range=(0, 256))
plt.subplot(2, 2, 3)
plt.title('Green Histogram')
plt.bar(bins_g[:-1], hist_g, color='green', width=1)

hist_b, bins_b = np.histogram(b.ravel(), bins=256, range=(0, 256))
plt.subplot(2, 2, 4)
plt.title('Blue Histogram')
plt.bar(bins_b[:-1], hist_b, color='blue', width=1)

plt.tight_layout()
plt.show()
