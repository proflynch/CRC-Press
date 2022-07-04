# Program_17c.py: Simple Backpropagation.
import numpy as np
w11,w12,w21,w22,w13,w23 = 0.2,0.15,0.25,0.3,0.15,0.1
b1 , b2 , b3 = -1 , -1 , -1
yt , eta = 0 , 0.1
x1 , x2 = 1 , 1
def sigmoid(v):
    return 1 / (1 + np.exp(- v))
h1 = x1 * w11 + x2 * w21 + b1
h2 = x1 * w12 + x2 * w22 + b2
o1 = sigmoid(h1) * w13 + sigmoid(h2) * w23 + b3
y = sigmoid(o1)
print("y = ", y)
# Backpropagate.
dErrdw13=(yt-y)*sigmoid(o1)*(1-sigmoid(o1))*sigmoid(h1)
w13 = w13 - eta * dErrdw13
print("w13 = ", w13)
dErrdw23=(yt-y)*sigmoid(o1)*(1-sigmoid(o1))*sigmoid(h2)
w23 = w23 - eta * dErrdw23
print("w23 = ", w23)


