from turtle import *

def dance(t):
    t.goto(0,0)
    t.color('red')
    t.begin_fill()
    for i in range(2):
        t.right(120)
        t.forward(193)
    t.goto(0,0)
    t.right(45)
    t.circle(50, 180)  
    t.right(150)
    t.circle(50, 180)
    t.end_fill()
    t.hideturtle()
