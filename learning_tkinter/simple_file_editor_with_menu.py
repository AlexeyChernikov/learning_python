import sys
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb

ex = lambda: sys.exit(0)

def insert_text():
    file_name = fd.askopenfilename()

    try:
        f = open(file_name, "r", encoding="utf-8")
        text.delete(1.0, END)
        text.insert(1.0, f.read())
    except FileNotFoundError:
        mb.showerror("Error", "File not found!")
    except:
        mb.showerror("Error", "Error while working with file!")
    else:
        f.close()
 
def extract_text():
    file_name = fd.asksaveasfilename()
    
    try:
        f = open(file_name, "w")
        f.write(text.get(1.0, END))
    except FileNotFoundError:
        mb.showerror("Error", "File not found!")
    except:
        mb.showerror("Error", "Error while working with file!")
    else:
        f.close()

def clear_text():
    res = mb.askyesno("Clear text", "Are you sure you want to clear the text?")

    if res:
        text.delete(1.0, END)

def clear(event):
    contextmenu.post(event.x_root, event.y_root)

root = Tk()
root.title("Menu")
mainmenu = Menu(root)
root.config(menu=mainmenu)

filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Open", command=insert_text)
filemenu.add_command(label="Save", command=extract_text)
filemenu.add_command(label="Exit", command=ex)

mainmenu.add_cascade(label="File", menu=filemenu)

contextmenu = Menu(tearoff=0)
contextmenu.add_command(label="Clear", command=clear_text)

text = Text(root, width=50, height=25)
text.bind('<Button-3>', clear)
text.grid(columnspan=2)

root.mainloop()