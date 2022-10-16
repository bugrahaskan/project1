import tkinter
from tkinter import messagebox

def Click():
    replay = messagebox.askquestion("Quit?", "Are you sure quitting?")
    if replay == "yes":
        skylight.destroy()

skylight = tkinter.Tk()
skylight.title("Skylight")
button1 = tkinter.Button(skylight, text="bye", command=Click, bg="#0000FF", fg="#0000FF") # bg doesnt show up in macOS buttons
button1.grid(column=4, row=4)
button2 = tkinter.Button(skylight, text="button 2",fg="blue")
button2.grid(column=3, row=5, columnspan=2)
skylight.mainloop()