# Program 11d.py: Box Counting a Binary Image.
import numpy as np
import matplotlib.pyplot as plt
from skimage import io 
import pylab as pl
Sierp_img = io.imread('Sierpinski.png')
plt.imshow(Sierp_img,cmap='gray', interpolation='nearest')
width, height, _ = Sierp_img.shape
binary = np.zeros((width, height))
for i, row in enumerate(Sierp_img):
    for j, pixel in enumerate(row):
        if pixel[0] < 220:
            binary[i, j] = 1
        else:
            binary[i, j] = 0
# Centre the image.
img = binary[70:410,120:540]
width, height = img.shape
# Pad the image.
maxD=max(width,height)
Dim=int(2**np.ceil(np.log2(maxD)))
PadRow = int(Dim-width)
PadCol=int(Dim-height)
image=np.pad(img,[(0,PadRow),(0,PadCol)],mode="constant")
fig=plt.figure()
plt.axis("off")
io.imshow(image)
pixels=[]
for i in range(Dim):
	for j in range(Dim):
		if image[i,j] ==1:  
			pixels.append((i,j))    
pixels=pl.array(pixels)   
 
scales=np.logspace(1, 8, num=20, endpoint=False, base=2)
Ns=[]
for scale in scales:
    H, edges=np.histogramdd(pixels,bins=(np.arange(0,Dim,scale),\
                            np.arange(0,Dim,scale)))
    Ns.append(np.sum(H > 0))
# Polyfit to a straight line.
coeffs=np.polyfit(np.log(scales), np.log(Ns), 1)
D = -coeffs[0]  # The fractal dimension.
fig=plt.figure()
plt.rcParams["font.size"] = "16"
print("The fractal dimension is ", D )
plt.plot(-np.log(scales),np.log(Ns), "o", mfc="none", \
         label="Box count data")
plt.plot(-np.log(scales), np.polyval(coeffs,np.log(scales)),\
         label="Line of best fit")
plt.xlabel("$-\log \ell$")
plt.ylabel("$\log N$")
plt.legend()
plt.show()