import tkinter as tk
from tkinter import *
root = tk.Tk()


#Make canvas with dimensions where 
canvas_width = 745
canvas_height = 745
w = Canvas(root, 
           width=canvas_width,
           height=canvas_height)
w.pack()
currentx = 0
lastx = 0
currenty = 0
lasty = 0
direction = 'left'
steps = 0
def motion(event):
    global lastx, lasty, currentx, currenty
    lastx= currentx
    lasty = currenty
    x, y = event.x, event.y
    currentx = x
    currenty = y
    if currentx <= lastx :
        direction = 'left'
        steps = lastx - currentx
    elif currentx > lastx :
        direction = 'right'
        steps = currentx - lastx
    print('%s %s' %(direction, steps))
    #print('%s , %s' % (posx, posy))

root.bind('<Motion>', motion)
root.mainloop()
