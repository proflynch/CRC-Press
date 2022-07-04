# Program_14b.py: Bifurcation diagram of the Ikeda map.
from matplotlib import pyplot as plt
import numpy as np
B , phi , Pmax , En = 0.15 , 0 , 10 , 0   # phi is a linear phase shift.
half_N = 99999
N = 2*half_N + 1
N1 = 1 + half_N
esqr_up, esqr_down = [], []
ns_up = np.arange(half_N)
ns_down = np.arange(N1, N)
# Ramp the power up
for n in ns_up:
    En = np.sqrt(n * Pmax / N1) + B * En * np.exp(1j*((abs(En))**2 - phi))
    esqr1 = abs(En)**2
    esqr_up.append([n, esqr1])
esqr_up = np.array(esqr_up)
# Ramp the power down
for n in ns_down:
    En = np.sqrt(2 * Pmax - n * Pmax / N1) + \
     B*En* np.exp(1j*((abs(En))**2 - phi))
    esqr1 = abs(En)**2
    esqr_down.append([N-n, esqr1])
esqr_down=np.array(esqr_down)
fig, ax = plt.subplots()
xtick_labels = np.linspace(0, Pmax, 6)
ax.set_xticks([x / Pmax * N1 for x in xtick_labels])
ax.set_xticklabels(["{:.1f}".format(xtick) for xtick in xtick_labels])
plt.plot(esqr_up[:, 0], esqr_up[:, 1], "r.", markersize=0.1)
plt.plot(esqr_down[:, 0], esqr_down[:, 1], "b.", markersize=0.1)
plt.xlabel("Input Power", fontsize=15)
plt.ylabel("Output Power", fontsize=15)
plt.tick_params(labelsize=15)
plt.show()