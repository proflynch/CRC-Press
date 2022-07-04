# Program_6b: Bifurcation diagram of the logistic map.
import numpy as np
import matplotlib.pyplot as plt 
def f(x, mu):
    return mu * x * (1-x)
xs , mus = [] , np.linspace(0, 4, 10000) 
for mu in mus:
  x = 0.1
  for i in range(500):
    x = f(x, mu)
  for i in range(50):
    x = f(x, mu)
    xs.append([mu, x])            
xs = np.array(xs) 
plt.plot(xs[:,0],xs[:,1],'r.',markersize=0.01) 
plt.xlabel("$\mu$",fontsize=15) 
plt.ylabel("x",fontsize=15) 
plt.tick_params(labelsize=15)
plt.show()
