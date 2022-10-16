from tkinter import *
from tkinter import messagebox

def validate(num):
    if isinstance(num, int) or isinstance(num, float):
        print("ok")
        return True
    else:
        return False


def click():
    try:
        assert validate(num1.get()) and validate(num2.get())
        if choice.get() == 1:
            res = num1.get() + num2.get()
            messagebox.showinfo("Summation", res)
        elif choice.get() == 2:
            res = num1.get() - num2.get()
            messagebox.showinfo("Substraction", res)
        elif choice.get() == 3:
            res = num1.get() * num2.get()
            messagebox.showinfo("Multiplication", res)
        elif choice.get() == 4:
            res = num1.get() / num2.get()
            messagebox.showinfo("Division", res)
    except TypeError:
        messagebox.showerror("Error", "You entered invalid arguments")
        print("ok")

calculator = Tk()
calculator.title("a Primitive Calculator")
#calculator.tk.call('wm', 'iconphoto', calculator._w, PhotoImage(file='moon.png'))

num1 = DoubleVar()
num2 = DoubleVar()
num1.set(0.0)
num2.set(0.0)


entry1 = Entry(calculator, textvariable=num1)
entry1.grid(column=0, row=1)

choice = IntVar()
choice.set(1)

button1 = Radiobutton(calculator, text="+", variable=choice, value=1)
button2 = Radiobutton(calculator, text="-", variable=choice, value=2)
button3 = Radiobutton(calculator, text="*", variable=choice, value=3)
button4 = Radiobutton(calculator, text="/", variable=choice, value=4)
button1.grid(column=1, row=0)
button2.grid(column=1, row=1)
button3.grid(column=1, row=2)
button4.grid(column=1, row=3)

entry2 = Entry(calculator, textvariable=num2)
entry2.grid(column=2, row=1)

evaluate = Button(calculator, text="Evaluate", command=click)
evaluate.grid(column=1, row=4)

calculator.mainloop()