from email.mime import application
from tkinter import *
from tkinter.tix import LabelEntry
from tkinter.ttk import Labelframe

application = Tk()


application.geometry('600x400+10+10')
application.resizable(False,False)
application.title('Demo App')
application.configure(bg='black')

top_panel = Frame(application)
top_panel.pack(side=TOP)

left_panel = Frame(application)
left_panel.pack(side=LEFT)

right_panel = Frame(application)
right_panel.pack(side=RIGHT)

footer_panel = Frame(application)
footer_panel.pack(side=BOTTOM)

title_tag = Label(top_panel,
                    text='this is an App',
                    fg='white',
                    bg='black',
                    font=('Courier',16))
title_tag.grid(row=0, column=0)

test_left = LabelFrame(left_panel, text='Test Left')
test_left.pack(side=LEFT)




application.mainloop()