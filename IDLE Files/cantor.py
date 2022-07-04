# Cantor Set
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
            y -= 50
            cantor3(x , y , length / 3)
            cantor3(x + 2 * length / 3 , y , length / 3)
            penup()
            setpos(x , y + 50)
