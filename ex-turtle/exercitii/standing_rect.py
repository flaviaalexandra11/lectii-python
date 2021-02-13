'''
    Standing rectangle
    Desenați un dreptunghi în picioare fară să folosiți instrucțiunea goto.
'''

import turtle

screen = turtle.Screen()
turtle = turtle.Turtle()

# latura jos: stanga -> dreapta
turtle.forward(50)

# latura dreapta: jos -> sus
turtle.left(90)
turtle.forward(100)

# latura sus: dreapta -> stanga
turtle.left(90)
turtle.forward(50)

# latura stanga: sus -> jos
turtle.left(90)
turtle.forward(100)

screen.mainloop()