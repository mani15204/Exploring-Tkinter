# Importing necessary libraries
import tkinter as tk
from tkinter import *
from tkinter.constants import *

# GUI Window
root = Tk()
root.title("Hello world")
root.geometry("500x500")

label = Label(root, text="Hello World")
label.pack()


# Let's try similar code - exploring grid
root2 = Tk()
root2.title("Second one")

label1 = Label(root2, text="When window size is not mentioned")
label1.grid(row=0, column=0, padx=0, pady=0)

root2.mainloop()


root.mainloop()