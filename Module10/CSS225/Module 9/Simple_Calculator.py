# Simple calculator with GUI
# Updated on: 12/7/2023
# Updated by: Ainur Emilbekova
#
#
# Imports Tkinter module, which provides tools for creating GUI applications
from tkinter import *
# Creates main window for the calculator
root = Tk()

root.title("Simple Calculator")

# Creates an Entry widget for displaying input and output
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Handles number button clicks
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

# Clears the display
def button_clear():
    e.delete(0, END)

# Captures the first operand, records the operator, and
# readies the display for the entry of the second operand
def button_operator(operator):
    first_number = e.get()
    global f_num
    global num_operator
    f_num = int(first_number)
    num_operator = operator
    e.delete(0, END)

# Completes the calculation by using the selescted operator and
# the second number inputted by the user. Then, shows the result in the
#calculator's display
def button_equal():
    # retrieves the current content of the dicplay
    second_number = e.get()
    # clears the display
    e.delete(0, END)
    if num_operator == '+':
        e.insert(0, f_num + int(second_number))
    elif num_operator == '*':
        e.insert(0, f_num * int(second_number))
    elif num_operator == '/':
        e.insert(0, f_num / int(second_number))
    elif num_operator == '-':
        e.insert(0, f_num - int(second_number))
    else:
        e.insert(0, "Invalid!!!")

# Creates buttons for the digits 0-9, the addition operator, the equal sign,
# and clears calculator's GUI
#
# NOTE: We did not cover Lambda functins in class. A Lambda Function
# in Python programming is an anonymous function
# or a function having no name. It is a small and restricted function
# having no more than one line. In the case below, the Lambda function code
# is calling the code/function button_click() with the numbers 0-9 as the
# parameter. Just like a normal function, a Lambda function can have multiple
# arguments with one expression.

button_1 =  Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 =  Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 =  Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 =  Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 =  Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 =  Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 =  Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 =  Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 =  Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 =  Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add =  Button(root, text="+", padx=39, pady=20, command=lambda: button_operator("+"))
button_equal =  Button(root, text="   =   ", padx=79, pady=20, command=button_equal)
button_clear =  Button(root, text="Clear", padx=79, pady=20, command=button_clear)


# Creates three additional buttons in calculator's GUI for subtraction,
# multiplication and division
button_subtract =  Button(root, text="-", padx=40, pady=20, command=lambda: button_operator("-"))
button_multiply =  Button(root, text="*", padx=40, pady=20, command=lambda: button_operator("*"))
button_divide =  Button(root, text="/", padx=40, pady=20, command=lambda: button_operator("/"))

# Specifies the layout of the buttons in the calculator's GUI using the grid method

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

# Runs and responses to user input by an ongoing loop
root.mainloop()