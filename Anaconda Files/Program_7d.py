# Program_7d.py: Common Ion Effect Silver Chloride and Potassium Chloride.
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
numpoints = 100
Ag_0 , AgCl2_0 , Cl_0 , K_0  = 0 , 0 , 0.1 , 0.1
initparams = (Ag_0 , Cl_0 , K_0)
def AgCl_sol(concentrations):
    (Ag, Cl, K) = concentrations
    firstEq = Ag * Cl - 1.82E-10
    secondEq = Ag + K - Cl
    thirdEq = K - K
    return[firstEq, secondEq, thirdEq]
solution = opt.fsolve(AgCl_sol,initparams)
solubility = "{:.2E}".format(solution[0])
print("When |KCl| is", K_0, "M, AgCl solubility is", solubility)
logxrange = np.logspace(-5, -1 , num = numpoints)
#Below are the starting points, with Ag+ = 0, K+ and Cl- = x-range
guess_array = tuple(zip(np.zeros(numpoints),logxrange,logxrange)) 
out_array , Ag_conc , Cl_conc , K_conc = [] , [] ,[] ,[]
for num in range(0 , numpoints):
    out_array.append(list(opt.fsolve(AgCl_sol,guess_array[num])))
    Ag_conc.append(out_array[num][0])
    Cl_conc.append(out_array[num][1])
    K_conc.append(out_array[num][2])
plt.plot(K_conc,np.log10(Ag_conc),"r.")
plt.title("AgCl solubility vs KCl concentration")
plt.xlabel("KCl concentration (Moles per litre)")
plt.ylabel("Log(AgCl) solubility")
plt.show()