import turtle
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

s = turtle.getscreen() # init screen
turtle.Screen().bgcolor('black')

p = turtle.Turtle() # init pen

p.speed(0) # super fast

for x in range(360):
    p.pencolor(colors[x % 6]) # set 6 different colors to 6 edges
    p.width(x // 100) # set pensize from thin to thick   
    p.forward(x) # draw 1 edge
    p.left(61) # turn left by 60 degrees for spiral effect

p.screen.mainloop() # pause for viewing