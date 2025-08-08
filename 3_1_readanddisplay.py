import numpy as np
import matplotlib.pyplot as plt

img = plt.imread('C:/Users/ASUS/Desktop/Python3/misc/5.3.01.tiff')
image_01 = plt.imread('C:/Users/ASUS/Desktop/Python3/misc/4.1.03.tiff')
img_02 = plt.imread('C:/Users/ASUS/Desktop/Python3/misc/indexed_GIF.gif')  

plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
plt.title("RGB Image")
plt.imshow(image_01)
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title("Grayscale Image")
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title("Indexed Image")
plt.imshow(img_02)
plt.axis('off')
plt.tight_layout()
plt.show()

