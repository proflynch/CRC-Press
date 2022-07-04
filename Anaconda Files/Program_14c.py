# Program_14c.py: Animation of a JJ limit cycle bifurcation. 
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
from scipy.integrate import odeint
from matplotlib import style
fig=plt.figure()
myimages=[]

BJ=1.2;Tmax=100;
def JJ_ODE(x, t):
    return [x[1],kappa-BJ*x[1]-np.sin(x[0])]
style.use("ggplot")           # To give oscilloscope-like graph. 
time = np.arange(0, Tmax, 0.1) 
x0=[0.1,0.1]
for kappa in np.arange(0.1, 2, 0.1):
    xs = odeint(JJ_ODE, x0, time)
    imgplot = plt.plot(np.sin(xs[:,0]), xs[:,1], "g-")
    myimages.append(imgplot)

my_anim=animation.ArtistAnimation(fig,myimages,interval=500,\
                                  blit=False,repeat_delay=100)
plt.rcParams["font.size"] = "18"
plt.xlabel("$\sin(\phi)$")
plt.ylabel("$\Omega$")
plt.show()