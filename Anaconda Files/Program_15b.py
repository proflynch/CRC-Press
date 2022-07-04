# Program_15b.py: Markov Chain.
import numpy as np
import matplotlib.pyplot as plt
T = np.array([[2/10,4/10,1/10,3/10], \
              [1/15,5/15,8/15,1/15], \
              [5/18,9/18,3/18,1/18], \
              [3/17,6/17,2/17,6/17]    
              ])
n = 20
v=np.array([[0.25, 0.25, 0.25 , 0.25]])
print(v)
vHist = v

for x in range(n):
  v = np.dot(v , T).round(2)
  vHist = np.append(vHist , v , axis = 0)
  if np.array_equal(vHist[x] , vHist[x-1]):
      print("Steady state after" , x , "iterations.")
      break
  print(v)
plt.rcParams["font.size"] = "16"
plt.xlabel("Number of iterations")
plt.ylabel("Probablilities")
plt.plot(vHist)
#plt.rcParams['linecolor']
plt.legend(["$p_1$","$p_2$","$p_3$","$p_4$"],loc="best")
plt.show()
