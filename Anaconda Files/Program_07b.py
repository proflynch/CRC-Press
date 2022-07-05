# Program_7b.py: Production of Nitrogen Dioxide.
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
k , a0 , b0 , c0 = 0.00713 , 4 , 1, 0
def ode(c , t):
  dcdt = k * (a0 - c)**2 * (b0 - c / 2)
  return dcdt
t = np.linspace(0 , 400 , 401) # t=[0,1,2,...,400]
c = odeint(ode , c0 , t)
plt.xlabel("Time (s)")
plt.ylabel("c(t) (Ml$^{-1})$")
plt.title("Production of Nitrogen Dioxide")
plt.plot(t , c)
print("c(100) = ", c[100], "Moles per litre")
plt.show()