# Progfram_8b.py: Maximize Profit.
# Maximize P = 5x+12y, given 20x+10y<=2000, 10x+20y<=1200,10x+30y<=1500.
# x,y >= 0.
import numpy as np
import matplotlib.pyplot as plt
m = np.linspace(0,200,200)
x , y = np.meshgrid(m , m)
plt.imshow( ((x>=0) & (y>=0) & (20*x+10*y<=2000) & (10*x+20*y<=1200) & (10*x+30*y<=1500)).astype(int) , 
                extent=(x.min(),x.max(),y.min(),y.max()),origin="lower", cmap="Greys", alpha = 0.3)

# Plot the constraint lines.
x = np.linspace(0, 200, 200)
y1 = (-20*x+2000) / 10
y2 = (-10*x+1200) / 20
y3 = (-10*x+1500) / 30
plt.rcParams["font.size"] = "14"
plt.plot(x, y1, label=r"$20x+10y \leq 2000$", linewidth = 5)
plt.plot(x, y2, label=r"$10x+20y \leq 1200$",linewidth = 5)
plt.plot(x, y3, label=r"$10x+30y \leq 1500$",linewidth = 5)
# plt.plot(x , (-5 * x + 660) / 12 , label = r"$P_{max}=5x+12y$")
plt.xlim(0,150)
plt.ylim(0,100)
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()