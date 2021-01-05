#################### Turtle - fillcolor ####################

import turtle

s = turtle.Screen()
t = turtle.Turtle()
t.speed(2)
t.pensize(2)

# setare culoare creion
t.color("pink")

# setare culoare de umplere
t.fillcolor("cyan")


# incepem figura ce va fi umpluta
t.begin_fill()
t.goto(0, 0)

t.pendown()

t.goto(0, 100)
t.goto(100, 100)
t.goto(100, 0)
t.goto(0, 0)

# terminam figura ce va fi umpluta
t.end_fill()

t.hideturtle()
s.mainloop()
