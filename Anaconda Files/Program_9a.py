# Program_9a.py: Cobb-Douglas Model of Production.
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols , diff , solve 
L,K,lam=symbols("L K lam")
Lmax , Kmax  = 2000 , 200 
w , r = 20 , 170
Y = 200*L**(2/3)*K**(1/3)
C=10000
Lagrange=Y-lam*(w*L+r*K-C)
L1 = diff(Lagrange,L)
L2 = diff(Lagrange,K)
L3 = w*L+r*K-C
sol=solve([L1,L2,L3],L,K,lam)
Y1 = 200*sol[0][0]**(2/3)*sol[0][1]**(1/3)
C=20000
Lagrange=Y-lam*(w*L+r*K-C)
L1 = diff(Lagrange,L)
L2 = diff(Lagrange,K)
L3 = w*L+r*K-C
sol=solve([L1,L2,L3],L,K,lam)
Y2 = 200*sol[0][0]**(2/3)*sol[0][1]**(1/3)
Llist = np.linspace(0,Lmax, 1000)
Klist = np.linspace(0, Kmax, 120)
L, K = np.meshgrid(Llist, Klist)
plt.figure()
Z = 200*L**(2/3)*K**(1/3)
plt.contour(L,K,Z,[Y1,Y2],colors="red")
Z = 20*L+170*K
plt.contour(L,K,Z,[10000,20000],colors="blue")
plt.xlabel("L",fontsize=15)
plt.ylabel("K",fontsize=15)
plt.tick_params(labelsize=15)
plt.show()