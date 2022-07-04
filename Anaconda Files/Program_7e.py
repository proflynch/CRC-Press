#Below is my starting points, with Ag+ = AgCl2- = 0, K+ and Cl- = x-range
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
initAg , initAgCl2, initCl , initK , datapts = 0 ,0 , 0.1 , 0.1 , 100
logxrange = np.logspace(-5 , -1 , num = datapts)
initparams = (initAg, initAgCl2, initCl, initK)
def AgCl_sol2(concentrations):
    (Ag_conc2, AgCl2_conc2, Cl_conc2, K_conc2) = concentrations
    firstEq = Ag_conc2 * Cl_conc2 - 1.82E-10
    secondEq = AgCl2_conc2 - Ag_conc2 * Cl_conc2 ** 2 * 1.78E5
    thirdEq = Ag_conc2 + K_conc2 - Cl_conc2 - AgCl2_conc2
    fourthEq = K_conc2 - K_conc2
    return[firstEq, secondEq, thirdEq, fourthEq]
solution = opt.fsolve(AgCl_sol2,initparams)
solubility = "{:.2E}".format(solution[0] + solution[1])
print("At a KCl concentration of", initK, "AgCl solubility is", solubility)
datapts=100
guess_array2 = tuple(zip(np.zeros(datapts),np.zeros(datapts),logxrange,logxrange))
out_array2 = []
silver_conc2 = []
silverchloride_conc2 = []
chloride_conc2 = []
potassium_conc2 = []

for num in range(0,datapts):
    out_array2.append(list(opt.fsolve(AgCl_sol2,guess_array2[num])))
    silver_conc2.append(out_array2[num][0])
    silverchloride_conc2.append(out_array2[num][1])    
    chloride_conc2.append(out_array2[num][2])
    potassium_conc2.append(out_array2[num][3])

total_solubility = np.add(silver_conc2, silverchloride_conc2)

plt.plot(potassium_conc2,np.log10(total_solubility),'r.')
plt.title("Silver chloride concentration")
plt.xlabel('KCl concentration (Moles per litre)')
plt.ylabel('Log(solubility of AgCl)')
plt.savefig('Fig7.4.eps')
plt.show()