################# Turtle - speed, size, goto, penup/down #################

import turtle

s = turtle.Screen()
t = turtle.Turtle()

# setare viteza desenare
t.speed(1)

# setare grosime creion
t.pensize(2)

# ridica creionul(cursorul) de pe canvas
t.penup()

# muta creionul (cursorul) la coorodonatele (0, 0)
t.goto(0, 0)

# pune creionul inapoi pe canvas
t.pendown()

t.goto(0, 100)

# ascunde cursorul
t.hideturtle()
s.mainloop()