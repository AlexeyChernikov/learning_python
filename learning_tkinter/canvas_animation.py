from tkinter import *


xmouse, ymouse = None, None


def event_handler(event):
    global xmouse, ymouse
    xmouse, ymouse = event.x+25, event.y+25

    if xmouse < 50:
        xmouse = 52
    elif xmouse > 400:
        xmouse = 400

    if ymouse < 50:
        ymouse = 52
    elif ymouse > 400:
        ymouse = 400

    move_ball()

def move_ball():
    x = c.coords(ball)[2]
    y = c.coords(ball)[3]

    if x < xmouse:
        x = 1
    elif x == xmouse:
        x = 0
    else:
        x = -1
    
    if y < ymouse:
        y = 1
    elif y == ymouse:
        y = 0
    else:
        y = -1

    c.move(ball, x, y)

    if c.coords(ball)[2] != xmouse or c.coords(ball)[3] != ymouse:
        c.after(10, move_ball)


root = Tk()
c = Canvas(root, width=400, height=400, bg='white')
c.pack()
ball = c.create_oval(5, 5, 55, 55, fill='green')
c.bind('<Button-1>', event_handler)

root.mainloop()