from email import message
import tkinter as tk
from tkinter import messagebox

def clicked(event=None):
    tk.messagebox.showinfo("My Title","show info\n over here")

window = tk.Tk()

label = tk.Label(window, text="This is a label")
label.bind("<Button-1>", clicked)
label.pack()

frame = tk.Frame(window, height=50, width=100, bg="#0000FF")
frame.pack()

button = tk.Button(window, text="mute button", command=clicked)
button.pack(fill=tk.X)

switch = tk.IntVar()
switch.set(1)

check = tk.Checkbutton(window, text="check the button", variable=switch)
check.pack()

entry = tk.Entry(window, width=30)
entry.pack()

radiobutton1 = tk.Radiobutton(window, text="Choice 1", variable=switch, value=0)
radiobutton2 = tk.Radiobutton(window, text="Choice 2", variable=switch, value=1)
radiobutton1.pack()
radiobutton2.pack()

window.mainloop()