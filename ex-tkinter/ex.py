from tkinter import *

# dimensiuni pentru fereastra & canvas
HEIGHT = 600
WIDTH = 1000

# cream o fereastra
window = Tk()
# setam o dimnesiune minima pentru fereastra
window.minsize(WIDTH, HEIGHT)
# setam fereastra sa nu poata fi redimensionata
window.resizable(False, False)

# cream un canvas
canvas = Canvas(width=WIDTH, height=HEIGHT)
canvas.pack()

# creare obiect de tip PhotoImage
image1 = PhotoImage(file="winter-images/flake.png")
# creare imagine in canvas
flake1 = canvas.create_image(100, 100, image=image1)

# la fiecare secunda, mutam imaginea din canvas
for time in range(1000, 20000, 1000):
    print("time: {}".format(time))
    window.after(time, lambda: canvas.move(flake1, 0, 10))

window.mainloop()