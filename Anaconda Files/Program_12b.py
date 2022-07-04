# Program_12b.py: Counting coloured pixels.
from skimage import io
import numpy as np
import matplotlib.pyplot as plt
peppers = io.imread("peppers.jpeg")
plt.figure(1)
io.imshow(peppers)
print("Image Dimensions=" , peppers.shape)
print("peppers[100,100]=",peppers[400,400])
Red = np.zeros((700,700))
for i in range(700):
    for j in range(700):
        if peppers[j,i,0]>190 and peppers[j,i,1]<120 \
            and peppers[j,i,2]<170:
            Red[j,i]=1
        else:
            Red[j,i]=0
plt.figure(2)
plt.imshow(Red,cmap="gray")
pixel_count = int(np.sum(Red))
print("There are {:,} red pixels".format(pixel_count))