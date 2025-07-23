#Image Statistics
import numpy as np
import matplotlib.pyplot as plt

img1 = plt.imread('C:/Users/CSELAB-2/Desktop/Python3/misc/4.1.03.tiff')
print(img1.min())
print(img1.max())
print(img1.mean())


print(np.median(img1))
print(np.average(img1))
print(np.mean(img1))
print(np.std(img1))
print(np.var(img1))
