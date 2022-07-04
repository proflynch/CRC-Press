# Program_6c.py: Determining the stability of critical points.
from sympy import symbols , diff , Matrix
x , y = symbols("x y")
P , Q = x*(1-x/7)-6*x*y/(7+7*x) , 0.2*y*(1-0.5*y/x)
J = Matrix([[diff(P,x),diff(P,y)],[diff(Q,x),diff(Q,y)]])
JA=J.subs([(x,1),(y,2)])
eigJA=JA.eigenvals()
print(eigJA)
JB=J.subs([(x,7),(y,0)])
eigJB=JB.eigenvals()
print(eigJB)