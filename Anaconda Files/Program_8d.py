# Program_8d.py: Simplex Method for Maximize Problem.
from scipy.optimize import linprog
obj = [-1, 1, -3]         # Minimize -P = -x1 + x2 - 3x3.
                          # Maximize P = x1 - x2 + 3x3.
lhs_ineq = [[ 1,  1, 0],  # x1 + x2.
          [ 0, -1, -1]]   # - x2 - x3.

rhs_ineq = [20,   # Constraint inequality 1.
            -10]  # Constraint inequality 2.
lhs_eq = [[1, 0, 1]]  # x1 + x3.
rhs_eq = [5]       # Constraint equation.

bnd = [(0, float("inf")), (0, float("inf")) , (0, float("inf"))]  # Bounds of x1 , x2 , x3.

opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,
      A_eq=lhs_eq, b_eq=rhs_eq, bounds=bnd,
      method="revised simplex")
print(opt)