# Program_12c.py: Statistical Analysis on Microbes.
import matplotlib.pyplot as plt
from skimage import io , measure
import numpy as np
from skimage.measure import regionprops
from scipy import ndimage
from skimage import feature

microbes_img = io.imread("Microbes.png")
fig1 = plt.figure() # Original image.
plt.imshow(microbes_img,cmap="gray", interpolation="nearest")
width, height, _ = microbes_img.shape

fig2 = plt.figure() # Binary image.
binary = np.zeros((width, height))
for i, row in enumerate(microbes_img):
    for j, pixel in enumerate(row):
        if pixel[0] > 80:
            binary[i, j] = 1
plt.imshow(binary,cmap="gray")
print("There are {:,} white pixels".format(int(np.sum(binary))))
blobs = np.where(binary>0.5, 1, 0)
labels, no_objects = ndimage.label(blobs)
props = regionprops(blobs)
print("There are {:,} clusters of cells:".format(no_objects))

# fig3. Centroids of the clusters.
object_labels = measure.label(binary)
some_props=measure.regionprops(object_labels)
fig,ax = plt.subplots(1,1)
#plt.axis('off')
ax.imshow(microbes_img,cmap="gray")
centroids = np.zeros(shape=(len(np.unique(labels)),2))
for i , prop in enumerate(some_props):
    my_centroid = prop.centroid
    centroids[i,:]=my_centroid
    ax.plot(my_centroid[1],my_centroid[0],"r+")
#print(centroids)

fig4 = plt.figure() # Histogram of the data.
labeled_areas = np.bincount(labels.ravel())[1:]
print(labeled_areas)
plt.hist(labeled_areas,bins=no_objects)
plt.xlabel("Area",fontsize=15)
plt.ylabel("Number of clusters",fontsize=15)
plt.tick_params(labelsize=15)

fig5 = plt.figure() # Canny edge detector.
edges=feature.canny(binary,sigma=2,low_threshold=0.5)
plt.imshow(edges,cmap=plt.cm.gray)
plt.show()
