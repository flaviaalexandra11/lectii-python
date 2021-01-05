"""
    Choose your shape
    Să se citească un cuvânt reprezentând o figură geometrică
    (patrat, dreptunghi, triunghi, cerc) și să se deseneze o figura corespunzătoare în turtle.
"""

import turtle

s = turtle.Screen()
t = turtle.Turtle()
t.color("red")
t.fillcolor("orange")

figura = input("Alege figura geometrica: ")

t.begin_fill()

if figura == "patrat":
    t.penup()
    t.goto(-50, -50)
    t.pendown()
    t.goto(50, -50)
    t.goto(50, 50)
    t.goto(-50, 50)
    t.goto(-50, -50)
elif figura == "dreptunghi":
    t.penup()
    t.goto(-80, -50)
    t.pendown()
    t.goto(80, -50)
    t.goto(80, 50)
    t.goto(-80, 50)
    t.goto(-80, -50)
elif figura == "triunghi":
    t.penup()
    t.goto(-50, -50)
    t.goto(50, -50)
    t.goto(0, 50)
    t.goto(-50, -50)
elif figura == "cerc":
    t.penup()
    t.goto(-50, -50)
    t.circle(50)
else:
    print("Figura geometrica necunoscuta.")

t.end_fill()
s.mainloop()