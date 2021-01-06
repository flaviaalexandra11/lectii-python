from tkinter import *

window = Tk()

canvas = Canvas(width=360, height=200, bg="#fcfcfc")
canvas.create_line(0, 100, 400, 100, fill="red", width=2, dash=(20, 2))

canvas.create_oval(2, 2, 100, 200, fill="yellow", width=2)
canvas.create_rectangle(10, 10, 80, 80, fill="yellow", width=2)

coord = 10, 50, 240, 210
arc = canvas.create_arc(coord, start=0, extent=150, fill="blue")

canvas.pack()
window.mainloop()