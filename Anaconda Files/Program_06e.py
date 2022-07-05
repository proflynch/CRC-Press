# Program_6e.py: SIR Epidemic model.
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint 
# Set the parameters.
beta, gamma = 0.5, 0.1
S0, I0, R0, N = 999, 1, 0, 1000
tmax, n = 100, 1000
def SIR_Model(X, t, beta, gamma):
    S, I, R = X
    dS = - beta * S * I / N
    dI = beta * S * I / N - gamma * I
    dR = gamma * I
    return(dS, dI, dR)
t = np.linspace(0, tmax, n)
f = odeint(SIR_Model, (S0, I0, R0), t, args = (beta, gamma))
S, I, R = f.T
plt.figure(1)
plt.xlabel("Time (days)")
plt.ylabel("Populations")
plt.title("Susceptible-Infected-Recovered (SIR) Epidemic Model")
plt.plot(t, S, label = "S")
plt.plot(t, I, label = "I")
plt.plot(t, R, label = "R")
legend = plt.legend(loc = "best")
plt.show()