from tkinter import *
import random

tk = Tk()
canvas = Canvas(tk, width=500, height=400)
tk.title('Dennis')
canvas.pack()
canvas.create_line(0, 0, 500, 400)
canvas.create_rectangle(100, 100, 200, 250, fill='blue')
canvas.create_oval(10,40,300,50, fill='purple')
canvas.create_polygon(400,10,100,100,500,300, fill='yellow')

for i in range(20):
    x1 = random.randrange(400)
    y1 = random.randrange(200)
    x2 = random.randrange(100)
    y2 = random.randrange(600)
    canvas.create_rectangle(x1, y1, x2, y2)

canvas.mainloop()
