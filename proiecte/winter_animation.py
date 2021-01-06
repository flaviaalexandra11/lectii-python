from tkinter import *

HEIGHT = 600
WIDTH = 1000

window = Tk()
window.title("Christmas Card")
window.minsize(WIDTH, HEIGHT)
window.resizable(False, False)

canvas = Canvas(width=WIDTH, height=HEIGHT)
canvas.pack()

image1 = PhotoImage(file="winter-images/flake.png")
flake1 = canvas.create_image(100, 100, image=image1)

for time in range(1000, 10000, 1000):
    window.after(time, lambda: canvas.move(flake1, 0, 10))

window.mainloop()