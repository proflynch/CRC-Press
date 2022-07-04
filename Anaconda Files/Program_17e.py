# Program_17e.py: Stability Diagram of a Neuromodule.
import numpy as np
import matplotlib.pyplot as plt
# Set parameters.
b2 , w11 , w21 , alpha , beta = -1 , 1.5 , 5 , 1 , 0.1
xmin=5
x=np.linspace(-xmin,xmin,1000)
y=b2 + w21 * np.tanh(x)
def sech(x):
    return 1 / np.cosh(x)
w12=(1-alpha*w11*(sech(alpha*x))**2) / \
    (alpha*beta*w21*(sech(alpha*x))**2*(sech(beta*y))**2)
b1=x-w11*np.tanh(alpha*x)-w12*np.tanh(beta*y)
plt.plot(b1, w12, "b") # Bistable boundary.
w12=(1+alpha*w11*(sech(alpha*x))**2) / \
    (alpha*beta*w21*(sech(alpha*x))**2*(sech(beta*y))**2)
b1=x-w11*np.tanh(alpha*x)-w12*np.tanh(beta*y)
plt.plot(b1, w12, "r") # Unstable boundary.
w12=(-1) / \
    (alpha*beta*w21*(sech(alpha*x))**2*(sech(beta*y))**2)
b1=x-w11*np.tanh(alpha*x)-w12*np.tanh(beta*y)
plt.plot(b1, w12, "k") # Neimark-Sacker boundary.
plt.rcParams["font.size"] = "20"
plt.xlim(-10,10)
plt.ylim(-10,10)
plt.xlabel("$b_1$")
plt.ylabel("$w_{12}$")
plt.show()