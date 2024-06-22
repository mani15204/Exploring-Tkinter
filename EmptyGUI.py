# Importing necessary modules
import tkinter as tk
from tkinter import *
from tkinter.constants import *

'''

    Creating a GUI using Tkinter in python is very easy.
    It just takes two lines of code to build an empty GUI window.

    root = Tk()
    root.mainloop()

    But let's explore little more from this

'''


# Building an empty GUI
root = Tk()
root.title("Title")  # Giving a title to the GUI in window title bar
root.geometry("500x500") # Setting window length and width
root.config(bg='lightblue', cursor='pirate') # Just having fun with some crazy configuration possible
root.mainloop()