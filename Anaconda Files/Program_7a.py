# Program_7a.py: Compute the matrix null-space vector. 
from sympy import Matrix
# Construct the augmented matrix.
ACCM=Matrix([[1,1,0,0,0,1],\
          [1,0,0,2,0,0],\
          [0,3,0,0,1,0],\
          [0,0,1,0,2,0],\
          [0,1,1,0,0,1],\
          [0,0,0,0,0,1]])
print(ACCM)
invACCM=ACCM.inv() # Find the inverse matrix.
print(invACCM)
Nullv=invACCM.col(5) / min(abs(invACCM.col(5))) # Last column.
print(Nullv) # Scaled null-space vector.