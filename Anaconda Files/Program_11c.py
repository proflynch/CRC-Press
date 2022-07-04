# Program_11c.py: The Barnsley fern fractal.
import matplotlib.pyplot as plt
import random
x , y , N_Iterations = [0], [0], 80000
idx = 0
for i in range(1, N_Iterations):
   r = random.randint(1, 100)
   # Four transformations.
   if r==1:
      x.append(0)
      y.append(0.2 * y[idx]-0.12)
   if r >= 2 and r <= 84:
      x.append(0.845 * x[idx] + 0.035 * y[idx])
      y.append(-0.035 * x[idx] + 0.82 * y[idx] +1.6)
   if r>= 85 and r<= 93:
      x.append(0.2 * x[idx] - 0.31 * y[idx])
      y.append(0.255 * x[idx] + 0.245*(y[idx])+0.29)
   if r >= 93:
      x.append(-0.15 * x[idx] + 0.24 * y[idx])
      y.append(0.25 * x[idx] + 0.2 * y[idx] + 0.68)
   idx += 1
plt.figure()
plt.scatter(x, y, s = 0.01, color = "g")
plt.axis("off")
plt.savefig("Fern.png")
plt.show()