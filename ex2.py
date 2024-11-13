# make infinite circles, start with a small circle, then draw a bigger circle around it

from turtle import *

r = 10
x = 20
while True:
    circle(r)
    r = r + x
    
    up()
    left(90)
    back(x)
    right(90)
    down()