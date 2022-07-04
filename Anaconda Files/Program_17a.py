# Program_17a.py: ANN for an AND Gate.
import numpy as np
w1 , w2 , b = 20 , 20 , -30
def sigmoid(v):
    return 1 / (1 + np.exp(- v))
def AND(x1, x2):
    return sigmoid(x1 * w1 + x2 * w2 + b)
print("AND(0,0)=", AND(0,0))
print("AND(1,0)=", AND(1,0))
print("AND(0,1)=", AND(0,1))
print("AND(1,1)=", AND(1,1))