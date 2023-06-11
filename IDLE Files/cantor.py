# Cantor Fractal.
# Run Module and type >>> cantor(-400 , 200 , 729)
from turtle import *
def cantor(x , y , length):
        speed(0) # Fastest speed.
        if length >= 5: # Stop when length < 5.
            penup()
            pensize(2)
            pencolor("blue")
            setpos(x , y)
            pendown()
            fd(length)
            y -= 60 # Height difference.
            cantor(x , y , length / 3)
            cantor(x + 2 * length / 3 , y , length / 3)
            penup()
            setpos(x , y + 50)
