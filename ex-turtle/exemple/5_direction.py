################ Turtle - forward/backward, left/right ################

import turtle

s = turtle.Screen()
s.bgcolor("SkyBlue")

t = turtle.Turtle()
t.speed(2)
t.pensize(2)

t.color("violet")
t.fillcolor("pink")

t.left(45)
t.forward(100)

t.left(45)
t.forward(100)

t.circle(10)

# t.hideturtle()
s.mainloop()