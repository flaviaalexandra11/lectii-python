###################### Turtle - Fereastra simpla ######################

# adaugare modul turtle la program
import turtle

# setare titlu ferestrei
turtle.title("Hello, turtle!")

# creare fereastra
s = turtle.Screen()

# setare culoare fundal pt fereastra
s.bgcolor("SkyBlue")

# creare cursor
t = turtle.Turtle()

# setare forma & dimensiune cursor
t.shape("turtle")
t.turtlesize(2)

# deschidere fereastra
s.mainloop()