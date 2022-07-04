# Program_10c.py: An animation of Chua's circuit. 
from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib import style
import numpy as np
from scipy.integrate import odeint
fig=plt.figure()
myimages=[]
mo , m1 , Tmax = -1/7 , 2/7 , 50
def Chua(x, t):
    return [a*(x[1]-(m1*x[0]+(mo-m1)/2*(np.abs(x[0]+1)-\
    np.abs(x[0]-1)))),x[0]-x[1]+x[2],-15*x[1]]
style.use("ggplot")
time = np.arange(0, Tmax, 0.1) 
x0=[1.96,-0.0519,-3.077]
for a in np.arange(8, 11, 0.1):
    xs = odeint(Chua, x0, time)
    imgplot = plt.plot(xs[:,0], xs[:,1], "g-")
    myimages.append(imgplot)
anim=animation.ArtistAnimation(fig,myimages,interval=500,\
                                  blit=False,repeat_delay=500)
plt.show()
