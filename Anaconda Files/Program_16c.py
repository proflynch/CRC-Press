# Program_16c.py: Fitzhugh-Nagumo Set Reset Flip-Flop. 
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
# Input currents.
Ic = 1
def Input_1(t): 
    return 1*(t>1000)-1*(t>1500)
def Input_2(t): 
    return 1*(t>2000)-1*(t>2500)
def Ic1(t):
    return Ic*(t>10)
def Ic2(t):
    return Ic*(t>0)
# Constants
theta,gamma,epsilon,m,c,Tmax = 0.1,0.1,0.1,-100,60,2000      
w1 , x1 = 0.5 , -1
t=np.arange(0.0, 3000.0, 0.1)
# Inputs from neurons and outputs for O1 and O2.
def FN_ODEs(X,t):
    u1,v1,u2,v2,u3,v3,u4,v4=X
    du1 = -u1*(u1-theta)*(u1-1)-v1+Input_1(t)   
    dv1 = epsilon*(u1-gamma*v1)
    du2 = -u2*(u2-theta)*(u2-1)-v2+Input_2(t)          
    dv2 = epsilon*(u2-gamma*v2)
    du3 = -u3*(u3-theta)*(u3-1)-v3+w1/(1+np.exp(m*v1+c)) \
              +x1/(1+np.exp(m*v4+c)) + Ic1(t)
    dv3 = epsilon*(u3-gamma*v3)         
    du4 = -u4*(u4-theta)*(u4-1)-v4+0.45/(1+np.exp(m*v2+c)) \
              +x1/(1+np.exp(m*v3+c)) + Ic2(t)      
    dv4 = epsilon*(u4-gamma*v4)
    return du1,dv1,du2,dv2,du3,dv3,du4,dv4
    
X = odeint(FN_ODEs,[0.01,0.01,0.01,0.01,0,0,0,0],t,rtol=1e-6)
u1,v1,u2,v2 = X[:,0],X[:,1],X[:,2],X[:,3]
u3,v3,u4,v4 = X[:,4],X[:,5],X[:,6],X[:,7]
plt.rcParams["font.size"] = "20"
plt.subplots_adjust(hspace = 1)
plt.figure(1)
plt.subplot(4,1,1)
plt.title("Fitzhugh-Nagumo SR Flip-Flop")
plt.plot(t, u1, "b")
plt.ylim(-1, 1.5)
plt.ylabel("I$_1$")
plt.subplot(4,1,2)
plt.plot(t, u2, "b")
plt.ylim(-1, 1.5)
plt.ylabel("I$_2$")
plt.subplot(4,1,3)
plt.plot(t, u3, "g")
plt.ylim(0, 1)
plt.ylim(-1, 1.5)
plt.ylabel("O$_1$")
plt.subplot(4,1,4)
plt.plot(t, u4, "g")
plt.ylim(-1, 1.5)
plt.ylabel("O$_2$")
plt.xlabel("Time")
plt.show()