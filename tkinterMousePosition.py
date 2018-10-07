import tkinter as tk
from tkinter import *
root = tk.Tk()


#Make canvas with dimensions proportional to belt dimensions
canvas_width = 745
canvas_height = 745
w = Canvas(root, 
           width=canvas_width,
           height=canvas_height)
w.pack()
posx = 0
posy = 0
def motion(event):
    x, y = event.x, event.y
    posx = x
    posy = y
    print('%s , %s' % (posx, posy))

root.bind('<Motion>', motion)
root.mainloop()
