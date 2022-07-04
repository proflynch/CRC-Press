# Program_13d.py: The wave equation. Vibrating string.
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
U = np.zeros((101 , 3) , float)                  
k = range(0 , 101)
c=1
def init():                 # U[x,0] initial condition.
    for i in range(0, 81):
        U[i, 0] = 0.00125*i
        for i in range (81, 101):
            U[i, 0] = 0.1 - 0.005*(i - 80)            
def animate(num):                                
    for i in range(1, 100):
        U[i,2]=2*U[i,1]-U[i,0]+c**2*(U[i+1,1]-2*U[i,1]+U[i-1,1])
    line.set_data(k,U[k,2])                   
    for m in range (0,101):
        U[m, 0] = U[m, 1]
        U[m, 1] = U[m, 2]
    return line               
fig = plt.figure()  
ax = fig.add_subplot(111,autoscale_on=False,xlim=(0, 101),ylim=(-4, 4))
ax.grid()                                     
plt.title("Vibrating String")
line, = ax.plot(k, U[k,0], lw=2) 
plt.xlabel("x")
plt.ylabel("U(t,x)")                
for i in range(3,100):
    U[i,2] = 2*U[i,1]-U[i,0]+c**2*(U[i+1,0]-2*U[i,0]+U[i-1,0] )
anim = animation.FuncAnimation(fig, animate,init_func=init,frames= \
                               np.linspace(0,10,1000),interval=10,blit=False)          
plt.show()