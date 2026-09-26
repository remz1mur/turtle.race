from turtle import *
from random import randint
from pippi import *

t1 = Turtle()
t2 = Turtle()

def turtl(t, x, y, col):
    t.shape('turtle')
    t.color(col)
    t.penup()
    t.goto(x, y)

turtl(t1, -200, 20, 'pink')
turtl(t2, -200, -20, 'violet')

while t1.xcor() < 200 and t2.xcor() < 200:
    t1.forward(randint(2,10))
    t2.forward(randint(3,10))
    
maxx = max(t1.xcor(), t2.xcor())
if maxx == t1.xcor():
    print('Первая черепашка выиграла!')
    dance(t1)
else:
    print('Вторая черепашка выиграла!')
    dance(t2)
