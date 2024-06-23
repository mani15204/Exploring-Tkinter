# Importing modules
import tkinter as tk
from tkinter import *
from tkinter.constants import *

# GUI
root = Tk()
root.title("Handling Buttons")
root.geometry("500x500")

label = Label(root, text="Button Handling", font=("Times",20))
label.grid(row=0, column=0, padx=150, columnspan=4)

num=0
def clicked():
    global num
    num+=1
    lbl_clicked.config(text=f"Clicked {num} times :)")

btn = Button(root, text="Click here", command=clicked)
btn.grid(row=1, column=0)

lbl_clicked = Label(root, text="")
lbl_clicked.grid(row=1, column=1)

toggle_switch = True  # True - Yes;  False - No
def toggle():
    global toggle_switch
    toggle_switch = not toggle_switch
    lbl_toggle.config(text = "Enabled" if toggle_switch else "Disabled")

btn_toggle = Button(root, text="Toggle", command=toggle)
btn_toggle.grid(row=2, column=0)

lbl_toggle = Label(root, text="Enabled")
lbl_toggle.grid(row=2, column=1)

root.mainloop()