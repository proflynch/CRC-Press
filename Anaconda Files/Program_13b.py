# Program_13b.py: RK4 Method for an IVP.
import numpy as np
import matplotlib.pyplot as plt

f = lambda x, y: 1 - y     # The ODE.
h , y0 = 0.1 , 2           # Step size and y(0).
x = np.arange(0, 1 + h, h) # Numerical grid.
y , y[0] = np.zeros(len(x)) , y0

for n in range(0, len(x) - 1):
    k1=h*f(x[n] , y[n])
    k2=h*f(x[n] + h/2 , y[n] + k1/2)
    k3=h*f(x[n] + h/2 , y[n] + k2/2)
    k4=h*f(x[n] + h , y[n] + k3)
    k=(k1 + 2 * k2 + 2 * k3 + k4) / 6
    y[n+1] = y[n] + k
    
plt.rcParams["font.size"] = "16"
plt.figure()
plt.plot(x, y, "ro--", label="Numerical Solution")
plt.plot(x, np.exp(-x) + 1, "b", label="Analytical Solution")
plt.xlabel("x")
plt.ylabel("y(x)")
plt.grid()
plt.legend(loc="upper right")
plt.show()
