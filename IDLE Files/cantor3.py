# 1.4(a): Variation of the Cantor set.
# In Shell type >>> cantor3(-400 , 200 , 729)
from turtle import *
def cantor3(x , y , length):
    speed(0)
    if length >= 5:
        penup()
        pensize(2)
        pencolor("blue")
        setpos(x , y)
        pendown()
        fd(length)
        y -= 80
        cantor3(x , y , length / 5)
        cantor3(x + 2 * length / 5 , y , length / 5)
        cantor3(x + 4 * length / 5 , y , length / 5)
        penup()
        setpos(x , y + 80)
