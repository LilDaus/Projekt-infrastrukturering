from tkinter import *
import tkinter as tk
import matplotlib
import numpy as np
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sympy as sym
from sympy.parsing.sympy_parser import parse_expr


window = Tk()
# vindue størrelsen
window.geometry("700x700")

# her vætter vi titlen
window.title('udregner')


figure = Figure(figsize=(5, 5), dpi=100)
plot = figure.add_subplot(1, 1, 1)

def getFunctionFromString(inputString='y= x**2'):

    #Tjek efter om brugeren har tastet = ind i.
    if '=' in inputString:
        user_input = inputString.split('=')[1]  # Del input strengen op ved '=', og giv anden del tilbage.
    else:
        user_input=inputString

    x, y = sym.symbols('x y')

    expr = parse_expr(user_input)

    f = sym.lambdify([x], expr)

    return f

brugerens_input='x*x'

f = getFunctionFromString(brugerens_input)
X = np.arange(0,100,0.1)
Y = f(X)

plot.plot(X, Y, color="red")	# Plotting points

canvas = FigureCanvasTkAgg(figure, window)
canvas.get_tk_widget().grid(row=0, column=0)


window.mainloop()	# Running application