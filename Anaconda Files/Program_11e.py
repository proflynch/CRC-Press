# Program_11e.py: Cantor set multifractal.
from sympy import symbols, log, diff, plot
import matplotlib.pyplot as plt
from sympy.plotting import plot_parametric
plt.rcParams["font.size"] = "16"
p1 , p2 = 1 / 9 , 8 / 9
q , x = symbols("q x")
tau = log(p1**q + p2**q) / log(3)
alpha=-diff(tau , q)
f = alpha * q + tau
x = q
p1=plot_parametric(alpha , f ,  (q, -10, 10),xlabel=r'$\alpha$',
                   ylabel=r"$f(\alpha)$",show=False)
p2=plot(x, q, (x, 0, 0.7),line_color="r",show=False)
p1.append(p2[0])
p1.show()
