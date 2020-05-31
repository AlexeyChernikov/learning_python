from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
 
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
 
root = Tk()
root.title("Dialog windows")

text = Text(root, width=50, height=25)
text.grid(columnspan=2)

btns_frame = Frame(root)
btns_frame.grid(row=1, columnspan=2)

Button(btns_frame, text="Open", command=insert_text).grid(row=0, column=0, padx=2, pady=2)
Button(btns_frame, text="Save", command=extract_text).grid(row=0, column=1, padx=2, pady=2)
Button(btns_frame, text="Clear", command=clear_text).grid(row=0, column=2, padx=2, pady=2)
 
root.mainloop()