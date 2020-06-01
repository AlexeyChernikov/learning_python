import random
from tkinter import *


def new_place():
    new_x = random.random()
    new_y = random.random()
    btn.place(relx=new_x, rely=new_y, anchor=CENTER)
    

win_width = 400
win_height = 400

root = Tk()
root.title("Moving a button")
root.geometry(f'{win_width}x{win_height}+{root.winfo_screenwidth()//2-win_width//2}+{root.winfo_screenheight()//2-win_height//2}')

btn = Button(root, bg='green', activebackground='darkgreen', width=6, height=3, command=new_place)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()