# Numpy for color image

import numpy as np
import matplotlib.pyplot as plt
img1 = plt.imread('C:/Users/CSELAB-2/Desktop/Python3/misc/4.1.04.tiff')

print(img1[10, 10, 0])
print(img1[10, 10, 1])
print(img1[10, 10, 2])

print (img1[10, 10, :])


img2 = plt.imread('C:/Users/CSELAB-2/Desktop/Python3/misc/5.1.13.tiff')

print(img2[10, 10])


