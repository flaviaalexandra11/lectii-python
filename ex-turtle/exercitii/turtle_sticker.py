"""
    Ex: Turtle stickers
    Sa se citeasca o culoare (rosu, galben, verde, sau albastru)
    si o forma pentru cursor (in limba romana) si apoi sa se deseneze, folosind turtle,
    minim 3 stampile pe ecran cu forma si culoarea cerute de utilizator.
"""

import turtle

culoare = input("Intruduceti culoarea: ")
forma = input("Introduceti forma: ")

color = "black"
shape = "arrow"

if culoare == "rosu":
    color = "red"
elif culoare == "galben":
    color = "yellow"
elif culoare == "verde":
    color = "green"
elif culoare == "albastru":
    color = "blue"
else:
    print("Culoarea nu exista!")

if forma == "sageata":
    shape = "arrow"
elif forma == "patrat":
    shape = "sqare"
elif forma == "cerc":
    shape = "circle"
elif forma == "triunghi":
    shape = "triangle"
elif forma == "testoasa":
    shape = "turtle"
elif forma == "clasic":
    shape = "classic"
else:
    print("Forma nu exista!")

s = turtle.Screen()
s.bgcolor("skyBlue")

t = turtle.Turtle()
t.shape(shape)
t.fillcolor(color)
t.shapesize(3)
t.penup()

t.goto(-100, -50)
t.stamp()

t.goto(-50, 50)
t.stamp()

t.goto(0, -50)
t.stamp()

t.goto(50, 50)
t.stamp()

s.mainloop()