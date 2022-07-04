# Program_10e.py: Bifurcation diagram of the forced Duffing equation.
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
alpha , beta , k , omega = 1 , -1 , 0.1 , 1.25
rs_up , rs_down = [] , []
def Duffing(x, t):
    return [x[1],
            - k*x[1]-beta*x[0]-alpha*x[0]**3+gamma*np.cos(omega*t)]
num_steps , step = 20000 , 0.00002
interval = num_steps * step
x0, y0 = 1, 0
ns = np.linspace(0, num_steps, num_steps)
for n in ns: # Ramp up.
    gamma = step * n
    t = np.linspace(0, (4*np.pi) / omega, 200)
    xs = odeint(Duffing, [x0, y0], t)
    for i in range(2):
        x0 , y0 = xs[100, 0] , xs[100, 1]
        r = np.sqrt(x0**2 + y0**2)
        rs_up.append([n, r])
rs_up = np.array(rs_up)
for n in ns: # Ramp down.
    gamma = interval - step * n
    t = np.linspace(0, (4*np.pi) / omega, 200)
    xs = odeint(Duffing, [x0, y0], t)
    for i in range(2):
        x0 , y0 = xs[100, 0] , xs[100, 1]
        r = np.sqrt(x0**2 + y0**2)
        rs_down.append([num_steps - n, r])
rs_down = np.array(rs_down)
fig, ax = plt.subplots()
xtick_labels = np.linspace(0, interval, 5)
ax.set_xticks([x / interval * num_steps for x in xtick_labels])
ax.set_xticklabels(["{:.1f}".format(xtick) for xtick in xtick_labels])
plt.plot(rs_up[:, 0], rs_up[:,1], "r.", markersize=0.1)
plt.plot(rs_down[:, 0], rs_down[:,1], "b.", markersize=0.1)
plt.xlabel(r"$\Gamma$", fontsize=15)
plt.ylabel("r", fontsize = 15)
plt.tick_params(labelsize = 15)
plt.show()