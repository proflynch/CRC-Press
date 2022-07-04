# Program_6f.py: Create data for muscle model.
import numpy as np
import matplotlib.pyplot as plt
Length , a , b = 1200 , 380*0.098 , 0.325
F0 = a / 0.257         # Initial force.
vm , alpha , LSE0 , k = F0*b/a , F0/0.1 , 0.3 , a/25
t = [0+0.01*i for i in range(1201)]      # Time.
A = [1.001+0.001*i for i in range(100)]
B = [1.099-0.001*i for i in range(100)]
C = np.ones(100).tolist()
D = [0.999-0.001*i for i in range(100)]
E = [0.901+0.001*i for i in range(100)]
F = np.ones(100).tolist()
G = [1.001+0.001*i for i in range(100)]
H = [1.099-0.001*i for i in range(100)]
HH = np.ones(100).tolist()
J = [0.999-0.001*i for i in range(100)]
K = [0.901+0.001*i for i in range(100)]
KK = np.ones(101).tolist()
L = A+B+C+D+E+F+G+H+HH+J+K+KK         
plt.figure()
plt.plot(L)
plt.xlabel("Time (s)", fontsize=12)
plt.ylabel("Fraction of Muscle Length (L)", fontsize=12)
plt.tick_params(labelsize=12)
plt.show()
LSE = np.zeros(1200).tolist() # Length series element.
LCE = np.zeros(1200).tolist() # Length contractile element.
F = np.zeros(1201).tolist()   
for i in range(1200):         # Hill's ODEs.
    LSE[i] = 0.3 + F[i]/alpha
    LCE[i] = L[i] - LSE[i]
    dt = t[i+1] - t[i]
    dL = L[i+1] - L[i]
    dF = alpha*((dL/dt)+b*((F0-F[i])/(a+F[i])))*dt
    F[i+1] = F[i] + dF
F = np.array(F)
FF = (F0/100)*np.random.randn(1201)
F = F + FF
F = F.tolist()
plt.figure()
plt.plot(L,F)
plt.xlabel("Fraction of Muscle Length", fontsize=12)
plt.ylabel("Force ($mN/mm^2$)", fontsize=12)
plt.tick_params(labelsize=12)
plt.show()