from tkinter import *

# Creare window si entry
window = Tk()
window.title("Calculator")

entry = Entry(window, width=30, borderwidth=2, font="Arial 12")
entry.grid(row=0, column=0, columnspan=4, padx=0, pady=10)

# Variabilele pe care le vom folosi pentru calcul
first_number = None
second_number = None
result = None
operation = None


# Apasare pe buton cu cifra
def click_num(number):
    current = entry.get()                        # preia ce era in entry
    entry.delete(0, END)                         # sterge ce era in entry
    entry.insert(0, str(current) + str(number))  # concateneaza ce am mai apsat la entry


# Apasare pe buton de clear
def clear():
    global first_number
    global second_number
    global operation
    first_number = None     # goleste variabilele folosite
    second_number = None
    operation = None
    entry.delete(0, END)    # sterge ce este in entry


# Apasare pe buton cu operator
def update(my_op):
    global first_number
    global second_number
    global operation

    operation = my_op
    if entry.get() != "":
        first_number = int(entry.get())
    entry.delete(0, END)


def equal():
    global first_number
    global second_number
    global operation
    global result

    if entry.get() != "":
        second_number = int(entry.get())

    if operation == "A":
        result = first_number + second_number
    elif operation == "S":
        result = first_number - second_number
    elif operation == "M":
        result = first_number * second_number
    elif operation == "D":
        result = first_number / second_number

    entry.delete(0, END)
    entry.insert(0, str(result))

    first_number = result
    second_number = None
    result = None
    operation = None


# Definim butoanele
button_1 = Button(window, text='1', padx=40, pady=20, command=lambda: click_num(1))
button_2 = Button(window, text='2', padx=40, pady=20, command=lambda: click_num(2))
button_3 = Button(window, text='3', padx=40, pady=20, command=lambda: click_num(3))
button_4 = Button(window, text='4', padx=40, pady=20, command=lambda: click_num(4))
button_5 = Button(window, text='5', padx=40, pady=20, command=lambda: click_num(5))
button_6 = Button(window, text='6', padx=40, pady=20, command=lambda: click_num(6))
button_7 = Button(window, text='7', padx=40, pady=20, command=lambda: click_num(7))
button_8 = Button(window, text='8', padx=40, pady=20, command=lambda: click_num(8))
button_9 = Button(window, text='9', padx=40, pady=20, command=lambda: click_num(9))
button_0 = Button(window, text='0', padx=40, pady=20, command=lambda: click_num(0))

button_add = Button(window, text='+', padx=40, pady=20, command=lambda: update("A"))
button_subtract = Button(window, text='-', padx=40, pady=20, command=lambda: update("S"))
button_multiply = Button(window, text='*', padx=40, pady=20, command=lambda: update("M"))
button_divide = Button(window, text='/', padx=40, pady=20, command=lambda: update("D"))
button_equal = Button(window, text='=', padx=40, pady=20, command=equal)
button_clear = Button(window, text='C', padx=40, pady=20, command=clear)

# Punem butoanele pe ecran
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_divide.grid(row=1, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_multiply.grid(row=2, column=3)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_subtract.grid(row=3, column=3)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1)
button_equal.grid(row=4, column=2)
button_add.grid(row=4, column=3)

window.mainloop()