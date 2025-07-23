#Bitwise Operations

import numpy as np
import matplotlib.pyplot as plt

img1 = plt.imread('C:/Users/CSELAB-2/Desktop/Python3/misc/4.1.03.tiff')
img2 = plt.imread('C:/Users/CSELAB-2/Desktop/Python3/misc/4.1.04.tiff')

# logical AND
plt.imshow(np.bitwise_and(img1, img2))
plt. show()


# logical OR
plt.imshow(np.bitwise_or(img1, img2))
plt. show()


# logical XOR
plt. imshow(np.bitwise_xor (img2, img1))
plt. show ()

# logical NOT
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow (img1)
plt.subplot(1, 2, 2)
plt.title('Bitwise Image')
plt.imshow(np.bitwise_not(img1))
plt.show()
