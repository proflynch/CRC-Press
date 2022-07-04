# Program_14a.py: Fast Fourier transform of a noisy signal.
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft

Ns = 1000                    # Number of sampling points
Fs = 800                      # Sampling frequency
T = 1/Fs                      # Sample time
t = np.linspace(0, Ns*T, Ns)
amp1, amp2 , amp3 = 0.5 , 1 , 2
freq1, freq2 , freq3 = 60 , 120 , 30 

# Sum a 30Hz, 60Hz and 120 Hz sinusoid
x = amp1 * np.sin(2*np.pi * freq1*t) + amp2*np.sin(2*np.pi * freq2*t) \
    +amp3 * np.sin(2*np.pi * freq3*t)
NS = x + 0.5*np.random.randn(Ns)         # Add noise.
fig1 = plt.figure()
plt.plot(t, NS)
plt.xlabel("Time (ms)", fontsize=15)
plt.ylabel("NS(t)", fontsize=15)
plt.tick_params(labelsize=15)

fig2 = plt.figure()
Sf = fft(NS)
xf = np.linspace(0, 1/(2*T), Ns//2)
plt.plot(xf, 2/Ns * np.abs(Sf[0:Ns//2]))
plt.xlabel("Frequency (Hz)", fontsize=15)
plt.ylabel("$|NS(f)|$", fontsize=15)
plt.tick_params(labelsize=15)
plt.show()
