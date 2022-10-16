from tkinter import *
from tkinter import messagebox
from random import randint

def click(event=None):
    y2 = randint(1,150)
    x2 = randint(1,450)
    button.place(x=x2, y=y2)

window = Tk()
window.title("Catch me if you can")
window.geometry("500x200")

button = Button(window, text="Catch me!")
button.bind("<Enter>", click)
button.place(x=10, y=10)

window.mainloop()
