# Projekt-infrastrukturering


Her har vi vores trello https://trello.com/invite/b/JtIuVgjM/ae43df11d05710eb05ca86b42af3164e/projekt

Link til tkinter brug https://www.foxinfotech.in/2018/09/how-to-create-window-in-python-using-tkinter.html

vores synopsis viad [docs](https://docs.google.com/document/d/11HQmjYZEANnnKT7QOxXoVZlYtD3QBqFkWux2yL68lo0/edit?usp=sharing)


from numpy import *
import matplotlib.pyplot as plt

def cMode():
	print("CALCULATIONS MODE")
	prob = ""
	while prob != "q":
		try:
			print("Enter problem")
			prob = input()
			print(eval(bytes([ord(p) for p in prob])))
		except:
			if prob != "q":
				print("Invalid input")

def gMode():
	print("GRAPH MODE")
	eq, r1, r2 = "", 0, 0
	while eq != "q":
		try:
			print("Enter equation")
			eq = input()
			if eq == "q":
				break
			print("Enter range 1")
			r1 = input()
			if r1 == "q":
				break
			else:
				r1 = int(r1)
			print("Enter range 2")
			r2 = input()
			if r2 == "q":
				break
			else:
				r2 = int(r2)
			x = array(range(int(r1), int(r2)))
			y = eval(bytes([ord(p) for p in eq]))
			plt.plot(x, y)
			plt.show()
		except:
			if eq != "q":
				print("Invalid input")

mode = ""

while mode != "q":
	print(""" 
		1. c (Normal calculation)
		2. g (Graphing)
		3. q (Quit)
		""")
	mode = input().lower()
	if mode == "c":
		cMode()
	if mode == "g":
		gMode()
