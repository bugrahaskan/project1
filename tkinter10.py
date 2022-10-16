import tkinter as tk
import PIL


window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=400, bg='yellow')
canvas.create_line(10, 380, 200, 10, 380, 380, 10, 380)
canvas.create_rectangle(200, 100, 300, 300, outline='white', width=5, fill='red')
canvas.create_polygon(20,360,100,300,20,380)
canvas.create_oval(100, 100, 300, 200, outline='red', width=20, fill='white')
canvas.create_arc(200,100,300,300, width=5)
canvas.create_text(200, 200, text="Mary\nhad\na\nlittle\nlamb",
                   font=("Arial","40","bold"),
                   justify=tk.CENTER,
                   )
image = tk.PhotoImage(file="moon.png") # at parent directory
#canvas.create_image(10,10,image=image)

#jpg = PIL.Image.open('owl-mandala-owl-sticker.jpg')
#image = PIL.ImageTk.PhotoImage(jpg)
#canvas.create_image(200, 200, image=image)

button = tk.Button(window, text="Quit", command=window.destroy)
canvas.grid(row=0)
button.grid(row=1)
window.mainloop()
