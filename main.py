import tkinter as tk
import random as rd
from tkinter import messagebox as ms

class Main:
	def __init__(self):
		self.startEntry = None
		self.endEntry = None
	def gen(self):
		ms.showinfo('Number -:', rd.choice(range(int(self.startEntry.get()), int(self.endEntry.get())+1)))
	def sol(self):
		mainRoot = tk.Tk()
		mainRoot.geometry('600x400')
		mainRoot.config(bg = 'cyan')
		mainRoot.title('Random number generator')

		mainLabel = tk.Label(text = 'Generate a random numeric number -->', fg = 'black', bg = 'cyan', font = (40))
		startLabel = tk.Label(text = 'Starting Point -->', fg = 'white', bg = 'black', font = (28))
		endLabel = tk.Label(text = 'Ending Point -->', fg = 'white', bg = 'black', font = (28))
		self.startEntry = tk.Entry()
		self.endEntry = tk.Entry()
		btn = tk.Button(text = 'Generate', fg = 'white', bg = 'purple', command = self.gen)

		mainLabel.pack()
		startLabel.place(x = 200, y = 50)
		self.startEntry.place(x = 370, y = 55)
		endLabel.place(x = 200, y = 100)
		self.endEntry.place(x = 370, y = 105)
		btn.place(x = 300, y = 150)

		mainRoot.mainloop()


obj = Main()
obj.sol()
