#!/usr/bin/env bash
import tkinter
import math
from typing import Optional, Tuple

# Functions
def quadratic(a: float, b: float, c: float) -> Optional[Tuple[float, float]]:
    """ Solve the Quadratic Formula, and return the possibilities of X """
    result = []
    # Quadratic Formula
    # ax^2 + bx + c = 0
    #
    #        -b +- sqrt( b^2 - 4ac )
    #   x =  -----------------------
    #               2a
    r_inside_square = math.sqrt( # Solve portion inside square root
        (b * b) - ( 4 * a * c )
    )
    for i in [1, -1]:
        result.append(
            ( -b + (i * math.sqrt( # Top half of formula
                        ( b * 2 ) - ( 4 * a * c )
                    )
                ) 
            ) / ( 2 * a )
        )
    
    return (result[0], result[1],)

# Construct Window
## Window Properties
window = tkinter.Tk()
window.title("Quadratic Formula")
window.geometry("600x400")
window.minsize(300, 200)

## Labels
label_howto = tkinter.Label(window, text = 'Input your variables from a quadratic equation to get x.\nEnsure your equation is in the following format: \nax')

## Input

## Buttons

## Insert Widgets to Grid

# Present Window
window.mainloop()
