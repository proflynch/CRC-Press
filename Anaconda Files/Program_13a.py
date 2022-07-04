# Program_13a.py: Eulers Method for an IVP.
import numpy as np
import matplotlib.pyplot as plt

f = lambda x, y: 1 - y     # The ODE.
h , y0 = 0.1 , 2           # Step size and y(0).
x = np.arange(0, 1 + h, h) # Numerical grid.
y , y[0] = np.zeros(len(x)) , y0
for n in range(0, len(x) - 1):
    y[n + 1] = y[n] + h*f(x[n] , y[n])
plt.rcParams["font.size"] = "16"
plt.figure()
plt.plot(x, y, "ro--", label='Numerical Solution')
plt.plot(x, np.exp(-x) + 1, "b", label="Analytical Solution")
plt.xlabel("x")
plt.ylabel("y(x)")
plt.grid()
plt.legend(loc="upper right")
plt.show()