# Program_6a.py: Iteration of the logistic map function.
import numpy as np
import matplotlib.pyplot as plt
mu , x = 4 , 0.2            # For case (iv).
xs = [0.2]                  # Initially, 20% of the tank is full.
for i in range(50):
  x = mu * x * (1 - x)
  xs = np.append(xs , x)
  #print(x)                 # Print the x values if you like.
plt.plot(xs)
plt.xlabel("n")
plt.ylabel("$x_n$")
plt.show()