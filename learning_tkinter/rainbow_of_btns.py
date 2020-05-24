from tkinter import *


btns_colors = {
    "red": '#ff0000',
    "orange": '#ff7d00',
    "yellow": '#ffff00',
    "green": '#00ff00',
    "light blue": '#007dff',
    "blue": '#0000ff',
    "purple": '#7d00ff'
    }

        
class NewButton:
    def __init__(self, master, color, code_color):
        self.color = color
        self.code_color = code_color
        self.btn = Button(master, bg=self.code_color, activebackground=self.code_color, command=self.get_color)
        self.btn.pack(fill=X)

    def get_color(self):
        lbl["text"] = f"Color: {self.color}"
        tb.delete(0, END)
        tb.insert(0, self.code_color)


root = Tk()
root.title("Rainbow")
root.geometry('220x222')
root.resizable(False, False)

lbl = Label(root, text="Select color!", justify='center')
lbl.pack(fill=X)

tb = Entry(root, justify='center')
tb.pack(fill=X)

for k, v in btns_colors.items():
    NewButton(root, k, v)

root.mainloop()