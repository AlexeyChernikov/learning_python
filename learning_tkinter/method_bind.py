from tkinter import *


class App(Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.tb = Entry(self)
        self.tb.pack(side=LEFT, anchor=N)
        self.tb.bind('<Return>', self.add_in_list)
        self.tb.focus()

        self.lb = Listbox(self)
        self.lb.pack(side=LEFT)
        self.lb.bind('<Double-Button-1>', self.copy_to_entry)

    def add_in_list(self, event):
        self.lb.insert(END, self.tb.get())
        self.tb.delete(0, END)

    def copy_to_entry(self, event):
        self.tb.delete(0, END)
        self.tb.insert(0, self.lb.get(self.lb.curselection()))


root = Tk()
root.title("Method bind()")
root.resizable(False, False)
app = App(root)
root.mainloop()