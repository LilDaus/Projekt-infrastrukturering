from tkinter import *

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