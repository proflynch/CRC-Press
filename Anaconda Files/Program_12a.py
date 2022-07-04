# Program_12a.py: Generating a multifractal image.
import numpy as np
import matplotlib.pyplot as plt
from skimage import exposure, io, img_as_ubyte
p1, p2, p3, p4 = 0.1, 0.2, 0.3, 0.4         # See motif.
p = [[p1, p2], [p3, p4]]
for k in range(1, 9, 1):                      # 512x512 image.
    M = np.zeros([2 ** (k + 1), 2 ** (k + 1)])
    M.tolist()
    for i in range(2**k):
        for j in range(2**k):
            M[i][j] = p1 * p[i][j]
            M[i][j + 2**k] = p2 * p[i][j]
            M[i + 2**k][j] = p3 * p[i][j]
            M[i + 2**k][j + 2**k] = p4 * p[i][j]
    p = M
M = exposure.adjust_gamma(M, 0.2)             # Change the contrast.
plt.imshow(M, cmap="gray", interpolation="nearest")
im = np.array(M, dtype="float64")
im = exposure.rescale_intensity(im, out_range="float")
im = img_as_ubyte(im)
# Save the image as a portable network graphics (png) image.
io.imsave("Multifractal.png", im)
io.imshow(im)