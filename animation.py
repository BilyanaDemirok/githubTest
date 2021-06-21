from tkinter import *
import random
import time

#  dimensions of the drawing screen
WIDTH = 800
HEIGHT = 600

# Tk starts the built in Python interface

tk = Tk()    
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
tk.title('Pink ball animation')
canvas.pack()

top = canvas.create_oval(20, 20, 60, 60, fill='pink')
xspeed = 7
yspeed = 12

while True:
    canvas.move(top, xspeed, yspeed)
    pos = canvas.coords(top)
    if pos[3] >=HEIGHT or pos[1] <= 0:
        yspeed = -yspeed
    if pos[2] >= WIDTH or pos[0] <= 0:
        xspeed = -xspeed

    tk.update()
    time.sleep(0.01)

tk.mainloop()