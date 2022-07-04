# Program_12d.py: Vascular architecture tracing using ridge filters.
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage import color, data, filters
from skimage import morphology
retina_source = data.retina()

_, ax = plt.subplots()
ax.imshow(retina_source)

retina = color.rgb2gray(retina_source)
t0, t1 = filters.threshold_multiotsu(retina, classes=3)
mask = (retina > t0)
vessels = filters.sato(retina, sigmas=range(1, 10)) * mask
img_gray = rgb2gray(vessels)
t = 0.015
binary_mask = img_gray > t
fig, ax = plt.subplots()
binary_mask = morphology.remove_small_objects(binary_mask, 600)
plt.imshow(binary_mask, cmap="gray")
plt.show()