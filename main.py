#!/usr/bin/env bash
from re import L
import tkinter
import math
import time
from PIL import ImageTk, Image

# Functions
def quadratic(a: float, b: float, c: float):
    """ Solve the Quadratic Formula, and return the possibilities of X """
    # Quadratic Formula
    d = b**2-4*a*c # Discriminant

    if d < 0:
        print('No Real Solution')
        return None # No real solution
    elif d == 0:
        x = (-b+math.sqrt(b**2-4*a*c))/2*a # One Solution
        print(f'One Solution: {x}')
        return (x,)
    else:
        x1 = (-b + math.sqrt(d)) / (2 * a) # Two Solutions
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print(f'Two Solutions: {x1}, {x2}')
        return (x1,x2,)

def calculate():
    """ Get input and display result from quadratic() """
    for i in [input_a, input_b, input_c]: # Where there is no input, replace with 0
        if i.get() == '':
            i.delete(0, tkinter.END)
            i.insert(0, '0')
    
    label_solve.config(text = 'x = ?')
    time.sleep(0.5) # For percieved change in result when result is the same

    try:
        solution = quadratic(int(input_a.get()), int(input_b.get()), int(input_a.get()))
        label_err.config(text='')
    except ZeroDivisionError:
        label_err.config(text='Zero Division Error')
        return
    if solution == None:
        label_solve.config(text = f'No Real Solution.')
    elif len(solution) == 1:
        label_solve.config(text = f'x = {round(solution[0], 2)}')
    else:
        label_solve.config(text = f'x = {round(solution[0], 2)} or {round(solution[1], 2)}')

def validate(P):
    """ Validates Entry boxes, to only contain int """
    if str.isdigit(P) or P == "":
        return True
    else:
        return False

# Construct Window
## Window Properties
window = tkinter.Tk()
window.title("Quadratic Formula")
window.geometry("300x350")
window.minsize(300, 350)
window.iconbitmap('src/icon.ico')

call_validate = window.register(validate)

## Labels
label_howto = tkinter.Label(window, text = 'Quadtratic Formula\n\nInput your variables from a quadratic equation to get x.\nEnsure your equation is in the following format: \n')
label_equation = tkinter.Label(window, text = 'ax² + bx + c = 0\n', font = 'Monospace')
label_a = tkinter.Label(window, text = 'a =')
label_b = tkinter.Label(window, text = 'b =')
label_c = tkinter.Label(window, text = 'c =')

label_err = tkinter.Label(window, text = '', fg = '#ff0000')
label_solve = tkinter.Label(window, text = 'x = ?', fg = '#357ec7', font = 'Helvetica 18 bold')

## Input
input_a = tkinter.Entry(window, validate='all', validatecommand=(call_validate, '%P'))
input_b = tkinter.Entry(window, validate='all', validatecommand=(call_validate, '%P'))
input_c = tkinter.Entry(window, validate='all', validatecommand=(call_validate, '%P'))

## Buttons
button_calculate = tkinter.Button(
    window,
    text = 'Calculate',
    command = calculate,
)

## Images
image_equ = Image.open('src/equation.png')
image_resized = image_equ.resize((256,66))
imagetk_equ = ImageTk.PhotoImage(image_resized)
label_image = tkinter.Label(image=imagetk_equ)

## Insert Widgets to Grid
label_howto.grid(row=0, column=0, columnspan=2)
label_equation.grid(row=1, column=0, columnspan=2)

label_a.grid(row=2, column=0)
label_b.grid(row=3, column=0)
label_c.grid(row=4, column=0)

input_a.grid(row=2, column=1)
input_b.grid(row=3, column=1)
input_c.grid(row=4, column=1)

label_err.grid(row=5, column=0)
button_calculate.grid(row=5, column=1)

label_solve.grid(row=6, column=0, columnspan=2)

label_image.grid(row=7, column=0, columnspan=2)

# Present Window
window.mainloop()
