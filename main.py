#from sympy imort *
import numpy as np
from tkinter import *

window = Tk()

window.title("udregner")
window.configure(width=500, height=300)
window.configure(bg='lightgray')

winWidth = window.winfo_reqwidth()
winwHeight = window.winfo_reqheight()
posRight = int(window.winfo_screenwidth() / 2 - winWidth / 2)
posDown = int(window.winfo_screenheight() / 2 - winwHeight / 2)
window.geometry("+{}+{}".format(posRight, posDown))

window.mainloop()

#link til tkinter brug https://www.foxinfotech.in/2018/09/how-to-create-window-in-python-using-tkinter.html