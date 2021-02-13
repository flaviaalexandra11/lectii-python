"""
    Desenați folosind turtle și instrucțiunea for, o siprală triunghiulară.
    Hints:
        - latura: de la 200 la 0, scade cu 5
        - folosiți un unghi de 120 grade
        - folositi instructiunile forward si left
        - folosiți modul rgb și schimbați valorile lui r, g și b în for
    For fun: schimbați unghiul la 123.
"""

import turtle

screen = turtle.Screen()
screen.colormode(255)
# screen.bgcolor(0, 0, 0)

r = 250
g = 200
b = 50

t = turtle.Turtle()
t.pensize(2)
t.speed(10)
t.pencolor(r, g, b)

t.penup()
t.goto(-100, -100)
t.pendown()

for i in range(300, 0, -5):
    t.forward(i)
    t.left(120)
    if r > 0 and g > 0:
        r -= 5
        g -= 5
    if b < 255:
        b += 5
    t.pencolor(r, g, b)

screen.mainloop()