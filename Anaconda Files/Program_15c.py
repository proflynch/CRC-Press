# Program_15c.py: Animation of a Student-T Curve.
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import scipy.stats as stats
fig, ax = plt.subplots()
x = np.arange(-4 , 4 , 0.01)
y1 = stats.norm.pdf(x)
y2 = 0 * x
plt.plot(x , y1)

ax = plt.axis([-4 , 4 , 0 , 0.42])
Student_T, = plt.plot(x, y2) # Base line.

def animate(n):
    Student_T.set_data(x, stats.t.pdf(x, n))
    return Student_T,
# Create animation.
myAnimation = animation.FuncAnimation(fig, animate,frames=np.arange(0, 25, 0.1), \
                                      interval=1, blit=True, repeat=True)
plt.ylabel('Probability Densities')
plt.xlabel('Standard Deviations')
plt.rcParams["font.size"] = "20"
plt.show()