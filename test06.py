#Image Masks

import numpy as np
import matplotlib.pyplot as plt

img1 = plt.imread('C:/Users/CSELAB-2/Desktop/Python3/misc/4.1.03.tiff').copy()
nrows, ncols, channels = img1.shape
row, col = np.ogrid[:nrows, :ncols]
cnt_row, cnt_col = nrows / 2, ncols / 2
outer_disk_mask = ((row - cnt_row) ** 2 + (col - cnt_col) ** 2 > (nrows / 2) ** 2)
img1[outer_disk_mask] = 0
plt.imshow(img1)
plt.axis('off')
plt.title('Masked Image')
plt.show()
