# Program 10d.py: Two-mass, three-spring system.
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
# Set parameters and initial conditions
m1 , m2 , k1 , k2 , k3 = 1 , 2 , 1 , 2 , 3
x10, y10, x20, y20 = 0, 0, 1, 0
# Maximum time point and total number of time points
tmax, n = 20, 1001
def Mass_Spring(X, t, m1, m2, k1, k2, k3):
#The Differential Equations
    x1, y1, x2, y2 = X
    dx1 = y1 
    dy1 = -(k1 * x1 + k2 * (x1 - x2)) / m1
    dx2 = y2
    dy2 = -(k2*(x2 - x1) + k3 * x2) / m2
    return (dx1, dy1, dx2, dy2)
# Integrate differential equations on the time grid t.
t = np.linspace(0, tmax, n)
f = odeint(Mass_Spring, (x10, y10, x20, y20), t, args=(m1, m2, k1, k2, k3))
x1, y1, x2, y2 = f.T
plt.figure(1)
plt.xlabel("Time")
plt.ylabel("Displacement")
plt.title("Two-Mass, Three-Spring")
plt.plot(t, x1, label = "x1")
plt.plot(t, x2, label = "x2")
legend = plt.legend(loc = "best")
plt.show()