# Program_11f.py: Multifractal f(alpha) spectrum. 
from sympy import symbols, log, diff, plot
import matplotlib.pyplot as plt
from sympy.plotting import plot_parametric
plt.rcParams["font.size"] = "16"
p1 , p2 , p3 , p4 = 0.1 , 0.15 , 0.2 , 0.55
q , x = symbols("q x")
tau = log(p1**q + p2**q + p3**q + p4**q) / log(2)
alpha=-diff(tau , q)
f = alpha * q + tau
x = q
p1=plot_parametric(alpha , f ,  (q, -15, 10),xlabel=r'$\alpha$',
                   ylabel=r"$f(\alpha)$",show=False)
p2=plot(x, q, (x, 0, 2.2),line_color="r",show=False)
p1.append(p2[0])
p1.show()