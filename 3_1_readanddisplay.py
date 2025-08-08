import numpy as np
import matplotlib.pyplot as plt

image_01 = plt.imread('C:/Users/ASUS/Desktop/Python3/misc/4.1.03.tiff')

r = image_01.copy() 
g = image_01.copy()
b = image_01.copy()

r[:,:,[1,2]]=0
g[:,:,[0,2]]=0
b[:,:,[0,1]]=0

output = [image_01,r,g,b]
titles = ['image','RED','GREEN','BLUE']

for i in range(4):
    plt.subplot(1,4,i+1)
    plt.axis('off')
    plt.title(titles[i])
    plt.imshow(output[i])
    
plt.show()

