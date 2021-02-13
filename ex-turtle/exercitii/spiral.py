"""


"""

import turtle

sc = turtle.Screen()
sc.colormode(255)

r = 50
g = 250
b = 100

t = turtle.Turtle()
t.pencolor(r, g, b)
t.speed(5)

nr_laturi = int(input("Introduceti nr laturi: "))
lungime_lat = 300
unghi = 360 / nr_laturi

t.penup()
t.goto(-125, -125)
t.pendown()

while lungime_lat > 0:
    t.forward(lungime_lat)
    t.left(unghi)
    lungime_lat -= 5
    if r < 255:
        r = r + 5
    if g > 0:
        g = g - 5
    if b < 255:
        b = b + 2
    t.pencolor(r, g, b)

sc.mainloop()