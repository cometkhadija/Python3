#Arithmetic Operations

import numpy as np
import matplotlib.pyplot as plt

img1 = plt.imread('C:/Users/CSELAB-2/Desktop/Python3/misc/4.1.03.tiff')
img2 = plt.imread('C:/Users/CSELAB-2/Desktop/Python3/misc/4.1.04.tiff')
plt.imshow(img1)
#plt.show()
plt.imshow(img2)
#plt.show()

plt.imshow(img1 + img2)
plt .show()

plt.imshow(img1 - img2)
plt .show()

plt.imshow(img2 - img1)
plt .show()

plt.imshow(np.flip (img1, 0))
plt.show ()

plt.imshow(np.flip (img1, 1))
plt.show ()

plt.imshow(np.roll (img1, 2048))
plt.show ()

plt.imshow(np.fliplr (img1))
plt.show ()

plt.imshow(np.flipud (img1))
plt.show ()

plt.imshow(np.rot90 (img1))
plt.show ()
