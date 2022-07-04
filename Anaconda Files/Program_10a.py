# Program_10a.py: Current in a Resistor-Inductor-Capacitor circuit.
from sympy import symbols , diff , Eq , Function , dsolve , cos , plot
from matplotlib import style
t=symbols("t")
i=symbols("i",cls=Function) 
deqn1=Eq(i(t).diff(t,t) + 5*i(t).diff(t) + 6*i(t), 10*cos(t))
odesol1=dsolve(deqn1, i(t),ics={i(0): 0, diff(i(t), t).subs(t,0): 0})
print("i(t)=",odesol1.rhs)
style.use("ggplot")
plot(odesol1.rhs , (t , 0 , 20),xlabel = "Time", ylabel = "Current")