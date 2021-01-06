from tkinter import *

# creating window object with Tk class constructor
window = Tk()

# setting title for window
# window.title("Test")

# setting minimum size for window
# window.minsize(500, 200)
#
# # make window resizable on both axes (X and Y)
# window.resizable(True, True)
#
# # creating label1 (with image)
# image = PhotoImage(file="images/einstein.gif")
# label1 = Label(image=image).pack(side="left")
#
# # creating label2 (with text)
# explanation = "Use only GIF and PPM/PGM formats."
# label2 = Label(text=explanation).pack(side="right")

#############################################################

# # setting minimum size for window
# # window.minsize(200, 200)
#
# # make window resizable on both axes (X and Y)
# window.resizable(True, True)
#
# # creating labels & packing them to left
# label1 = Label(text="one", fg="white", bg="red").pack(side=LEFT)
# label2 = Label(text="two", fg="white", bg="green").pack(side=LEFT)
# label3 = Label(text="three", fg="white", bg="blue").pack(side=LEFT)
# label5 = Label(text="four", fg="white", bg="violet").pack(side=LEFT)

#############################################################

# # setting minimum size for window
# window.minsize(150, 150)
#
# # make window resizable on both axes (X and Y)
# window.resizable(True, True)
#
# # creating labels & packing them to left
# label1 = Label(text="Hello, Tkinter!", font="Arial 20", fg="navy")
# label1.pack(padx=20, pady=30)

#############################################################
#
# setting title for window
# window.title("Hello!")
#
# # setting minimum size for window
# window.minsize(150, 150)
#
# # make window resizable on both axes (X and Y)
# window.resizable(True, True)
#
# # creating labels & packing them to left
# label1 = Label(text="Hello, Tkinter!", font="Arial 20", fg="navy", bg="white")
# label1.pack(fill=Y)

#############################################################
# ACTIVITY HERE


# def print_entry_value():
#     value = entry.get()
#     print(value)
#
#
# entry = Entry(font="Arial 12", bg="white", fg="gray", bd=3, width=20)
# entry.pack()
#
# # button = Button(text="Print value!", command=print_entry_value)
# button = Button(text="Print value!", command=lambda: print(entry.get()))
# button.pack()
#
# def greet_me(param_name):
#     print("Hello, {}!".format(param_name))


# entry = Entry(font="Arial 12", bg="white", fg="gray", bd=3, width=20)
# entry.pack()
#
# button = Button(text="Greet mee!", command=lambda: greet_me(entry.get()))
# button.pack()
#
# name = "Alice"
# button = Button(text="Greet mee!", command=lambda: greet_me(name))
# button.pack()

#############################################################

# from tkinter import messagebox
#
# # messagebox.showerror("Title", "Error")
# # messagebox.showwarning("Title", "Warning")
# # messagebox.showinfo("Title", "Info")
#
# answer1 = messagebox.askokcancel("Title1", "Are you sure you want to leave?")
# print(answer1)
#
# answer2 = messagebox.askretrycancel("Title2", "Do you want to try again?")
# print(answer2)
#
# answer3 = messagebox.askyesno("Title3", "Yes or No?")
# print(answer3)

#############################################################

# from tkinter import simpledialog
#
# answer = simpledialog.askinteger("Input", "Input number", minvalue=0, maxvalue=100)
# print(answer)

#############################################################

# canvas = Canvas(width=360, height=200, bg="#fcfcfc")
# canvas.pack()

# canvas.create_line(0, 100, 200, 100, 200, 200, fill="red", width=2, dash=(20, 2))

# canvas.create_oval(2, 2, 100, 200, fill="yellow", width=2)

# canvas.create_arc(2, 2, 200, 200, start=0, extent=45, outline="black", fill="green", width=2)

# canvas.create_rectangle(5, 5, 200, 100, width=2, fill="violet", outline="red")

# canvas.create_text(150, 50, font="Arial 20", text="Hello, Canvas!")

#############################################################

# label1 = Label(window, text="1", fg="white", bg="red", padx=5, pady=5)
# label2 = Label(window, text="2", fg="white", bg="green", padx=5, pady=5)
# label3 = Label(window, text="3", fg="white", bg="blue", padx=5, pady=5)
# label5 = Label(window, text="4", fg="white", bg="violet", padx=5, pady=5)
#
# label1.grid(row=1, column=1)
# label2.grid(row=1, column=2)
# label3.grid(row=2, column=1)
# label5.grid(row=2, column=2)


# calling mainloop - creates the actual window
# window.mainloop()


############################ Canvas Events #################################

# Event with Mouse

# def mouse_fun(event):
#     print("clicked at: ({}, {})".format(event.x, event.y))
#
#
# canvas = Canvas(window, width=100, height=100)
# canvas.bind("<Button-1>", mouse_fun)
# canvas.pack()
#
# window.mainloop()

# Event with Keyboard

# def keyboard_fun(event):
#     print("key pressed: ", event.char)
#
#
# canvas = Canvas()
# canvas.focus_set()
# canvas.bind("<Key>", keyboard_fun)
# canvas.pack()
#
# window.mainloop()

