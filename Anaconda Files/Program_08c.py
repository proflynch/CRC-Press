# Program_8c.py: Simplex Method for Minimize Problem.
from scipy.optimize import linprog
obj = [20000, 25000]         # Minimize P = 20000x1 + 25000x2.
lhs_ineq = [[ -400,  -300],  # 400x1 + 300x2.
            [-300 , -400],   # 300x1 + 400x2
          [ -200, -500]]   #  200x1 + 500x2.

rhs_ineq = [-25000,   # Constraint inequality 1.
            -27000,
            -30000]  # Constraint inequality 2.

bnd = [(0, float("inf")), (0, float("inf")) ]  # Bounds of x1 , x2 , x3.

opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, bounds=bnd,
      method="revised simplex")
print(opt)