# Program_11a.py: The Koch Snowflake.
import numpy as np
import matplotlib.pyplot as plt
from math import floor
def Koch_Curve(k , angtri , xstart , ystart):
  n_lines , h = 4**k , 3**(-k)
  x, y, x[0],y[0] = [0]*(n_lines+1),[0]*(n_lines+1) , xstart , ystart                  
  segment=[0] * n_lines      
  angle=[0, np.pi/3, -np.pi/3, 0]  
  for i in range(n_lines):
    m , ang = i , angtri
    for j in range(k):
      segment[j] = np.mod(m, 4)
      m = floor(m / 4)
      ang = ang + angle[segment[j]]
    x[i+1] = x[i]+h*np.cos(ang)
    y[i+1] = y[i]+h*np.sin(ang)
  plt.axis("equal")
  plt.plot(x,y)
k = 6 # Plot the three sides.
Koch_Curve(k , np.pi/3 , 0 , 0)
Koch_Curve(k , -np.pi/3 , 0.5 , 0.866)
Koch_Curve(k , np.pi , 1 , 0)
plt.show()