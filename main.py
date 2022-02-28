from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)


# plot function is created for
# plotting the graph in
# tkinter window
def plot():

	# the figure that will contain the plot
	fig = Figure(figsize = (5, 5),dpi = 100)

	# list of squares
	y = [i**2 for i in range(10)]

	# subplot tilføjes
	plot1 = fig.add_subplot(111)

	# plot grafen
	plot1.plot(y)

# creating the Tkinter canvas
# containing the Matplotlib figure
	canvas = FigureCanvasTkAgg(fig,master = window)
	canvas.draw()

	# placing the canvas on the Tkinter window
	canvas.get_tk_widget().pack()

	# Matplotlib toolbar
	toolbar = NavigationToolbar2Tk(canvas,window)
	toolbar.update()

	#  toolbar i Tkinter window
	canvas.get_tk_widget().pack()

# the main Tkinter window
window = Tk()
# vindue størrelsen
window.geometry("700x700")

# her vætter vi titlen
window.title('udregner')


# den knap som man kan trykke på
plot_button = Button(master = window,command = plot,height = 3,width = 11,text = "Plot")

# place the button
# in main window
plot_button.pack()

window.mainloop()
