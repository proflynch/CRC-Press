# Program_13c.py: The Heat Equation. Modelling heat in a rod.
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
nt , nx , tmax , xmax , alpha = 1001 , 51 , 1 , 1 , 0.1
dt , dx = tmax/(nt-1) , xmax/(nx-1)
U , x = np.zeros((nx,nt)) , np.linspace(0, xmax, nx) # Initialize.
U[:,0] = np.sin(np.pi * x)                           # Initial conditions.
U[0,:] = U[-1,:] = 0                                 # Boundary conditions.
r = alpha * (dt / dx ** 2)
# Vectorized solution.
for n in range(nt-1):
    U[1:-1,n+1] = U[1:-1,n] + r * (U[2:,n] - 2 * U[1:-1,n] + U[:-2,n])
# Not vectorized commands using loops.
#for n in range(0,nt-1):
#  for i in range(0,nx-1):
#    U[0,n+1]=0
#    U[i,n+1] = U[i,n] + alpha*(dt/dx**2.0)*(U[i+1,n]-2.0*U[i,n]+U[i-1,n])
# for i in range(0 , nx):
#  x[i] = i * dx
plt.figure()
plt.rcParams["font.size"] = "16"
initial_cmap = cm.get_cmap("rainbow")
reversed_cmap=initial_cmap.reversed()
colour=iter(reversed_cmap(np.linspace(0 , 10 , nt)))
for i in range(0 , nt , 10):
  c=next(colour)
  plt.plot(x , U[:,i] , c = c)
plt.xlabel("x")
plt.ylabel("U(t,x)")
plt.ylim([0 , 1.2])
plt.show()