from tkinter import *

window = Tk()
window.title("Grid")

label0 = Label(text="My grid")
label0.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

label1 = Label(window, text="1", fg="white", bg="red", padx=5, pady=5)
label2 = Label(window, text="2", fg="white", bg="green", padx=5, pady=5)
label3 = Label(window, text="3", fg="white", bg="blue", padx=5, pady=5)
label4 = Label(window, text="4", fg="white", bg="violet", padx=5, pady=5)

label5 = Label(window, text="5", fg="white", bg="violet", padx=5, pady=5)
label6 = Label(window, text="6", fg="white", bg="blue", padx=5, pady=5)
label7 = Label(window, text="7", fg="white", bg="green", padx=5, pady=5)
label8 = Label(window, text="8", fg="white", bg="red", padx=5, pady=5)

label1.grid(row=1, column=0)
label2.grid(row=1, column=1)
label3.grid(row=1, column=2)
label4.grid(row=1, column=3)

label5.grid(row=2, column=0)
label6.grid(row=2, column=1)
label7.grid(row=2, column=2)
label8.grid(row=2, column=3)

window.mainloop()