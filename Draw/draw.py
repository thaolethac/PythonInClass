import turtle,random

color = ['red','green','blue']

painter = turtle.Turtle()

painter.pensize(3)
def choiceColor(x):
    if x <= 2:
        return x
    return choiceColor(x-3)
for i in range(20):
    painter.pencolor(color[choiceColor(i)])
    painter.circle(100)
    painter.right(30)
    painter.left(60)
    painter.setposition(0,0)
