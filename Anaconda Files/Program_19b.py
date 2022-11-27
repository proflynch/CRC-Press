# Program_19b.py: Contour and surface plots of the Hopfield Lyapunov
# function. Run in Spyder, in the Console window, type >>> matplotlib
# qt5. You can then rotate the 3D figures.
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
gamma = 0.7
def flux_qubit_potential(x,y):
    return -(x**2+y**2)- (4/(gamma*np.pi**2)) * \
    (np.log(np.cos(np.pi*x/2)) + np.log(np.cos(np.pi*y/2)))
y=np.linspace(-1,1,60)
x=np.linspace(-1,1,60)
X,Y=np.meshgrid(x,y)
Z=flux_qubit_potential(X,Y).T
fig=plt.figure(figsize = (10,10))
plt.subplot(1,2,1)
ax=fig.add_subplot(1,2,1,projection="3d")
p=ax.plot_wireframe(X, Y, Z, rstride=3, cstride=3)
ax.plot_surface(X,Y,Z,rstride=3,cstride=3,alpha=0.1)
 
ax.set_xlim3d(-1, 1);
ax.set_ylim3d(-1, 1);
ax.set_zlim3d(-0.2, 0);
ax.set_xlabel("$a_1$", fontsize = 15)
ax.set_ylabel("$a_2$", fontsize = 15)
ax.set_zlabel("$V$", fontsize = 15)
plt.tick_params(labelsize = 15)
plt.show()
plt.subplot(1,2,2)
plt.contour(X,Y,Z,[-0.1,-0.06,-0.05,-0.04,-0.02,-0.01,0.05])
plt.xlabel(r"$a_1$",fontsize=15)
plt.ylabel(r"$a_2$",fontsize=15)
plt.tick_params(labelsize=15)
plt.show()