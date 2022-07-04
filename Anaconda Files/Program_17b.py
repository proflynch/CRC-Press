# Program_17b.py: ANN for an OR Gate.
import numpy as np
w1 , w2 , b = 20 , 20 , -10
def sigmoid(v):
    return 1 / (1 + np.exp(- v))
def OR(x1, x2):
    return sigmoid(x1 * w1 + x2 * w2 + b)
print("OR(0,0)=", OR(0,0))
print("OR(1,0)=", OR(1,0))
print("OR(0,1)=", OR(0,1))
print("OR(1,1)=", OR(1,1))

