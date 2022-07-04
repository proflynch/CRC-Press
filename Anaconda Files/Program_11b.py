# Program_11b.py: The Sierpinski triangle and the chaos game.
import matplotlib.pyplot as plt
from random import random, randint
import numpy as np
def midpoint(P, Q):
    return (0.5*(P[0] + Q[0]), 0.5*(P[1] + Q[1]))
# The three vertices A,B,C.
vertices = [(0, 0), (2, 2*np.sqrt(3)), (4, 0)]
iterates = 100000
x, y = [0]*iterates, [0]*iterates
x[0], y[0] = random(), random()
for i in range(1, iterates):
    k = randint(0, 2)
    x[i], y[i] = midpoint(vertices[k], (x[i-1], y[i-1]))
#fig, ax = plt.subplots(figsize=(6, 6))
#ax.scatter(x, y, color='k', s=0.1)
#ax.axis('off')
fig=plt.figure()
plt.scatter(x,y,s=0.001,c="k")
plt.axis("off")
plt.axis("equal")
plt.savefig("Sierpinski.png")
plt.show()