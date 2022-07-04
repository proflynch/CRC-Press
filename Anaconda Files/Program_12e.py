# Program_12e.py: Segmentation of a human brain.
import matplotlib.pyplot as plt
from skimage import color
from skimage import morphology
from skimage import segmentation
import matplotlib.image as img

num_segs , threshold = 100 , 0.82
img =img.imread("Brain.jpg")

# Compute a mask
lum = color.rgb2gray(img)
mask = morphology.remove_small_holes(
    morphology.remove_small_objects(lum > threshold , 500) , 500)
mask = morphology.opening(mask, morphology.disk(3))

# SLIC result
slic = segmentation.slic(img, n_segments=num_segs, start_label=1)

# SLIC result in Mask
m_slic = segmentation.slic(img, n_segments=num_segs, mask=mask, \
start_label=1)

# Display result
fig, ax_arr = plt.subplots(2, 2, sharex=True, sharey=True, \
figsize=(10, 10))
ax1, ax2, ax3, ax4 = ax_arr.ravel()
ax1.imshow(img)
ax1.set_title("Brain.jpg")
ax2.imshow(mask, cmap="gray")
ax2.set_title("Mask")
ax3.imshow(segmentation.mark_boundaries(img, slic))
ax3.contour(mask, colors="red", linewidths=1)
ax3.set_title("SLIC")
ax4.imshow(segmentation.mark_boundaries(img, m_slic))
ax4.contour(mask, colors="red", linewidths=1)
ax4.set_title("SLIC in Mask")
for ax in ax_arr.ravel():
    ax.set_axis_off()
plt.tight_layout()
plt.show()
