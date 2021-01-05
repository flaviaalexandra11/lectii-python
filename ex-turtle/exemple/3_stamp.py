#################### Turtle - stamp ####################

import turtle

s = turtle.Screen()
s.bgcolor("SkyBlue")

t = turtle.Turtle()
t.shape("turtle")
t.turtlesize(2)

t.color("pink")
t.fillcolor("cyan")

t.penup()

# mutam si imprimam forma cursorului
t.goto(-100, -100)
t.stamp()

t.goto(0, 0)
t.stamp()

s.mainloop()