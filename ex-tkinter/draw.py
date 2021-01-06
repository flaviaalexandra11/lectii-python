from tkinter import *


def paint(event):
    x1 = (event.x - 1)
    y1 = (event.y - 1)
    x2 = (event.x + 1)
    y2 = (event.y + 1)
    canvas.create_oval(x1, y1, x2, y2, fill="#476042")


window = Tk()
window.title("Painting using Ovals")
canvas = Canvas(window, width=500, height=200)
canvas.pack()
canvas.bind("<B1-Motion>", paint)

message = Label(window, text="Press and Drag the mouse to draw")
message.pack(side=BOTTOM)

mainloop()

