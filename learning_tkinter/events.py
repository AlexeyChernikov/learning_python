from tkinter import *
 

class App(Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        self.pack(padx=2)
        self.create_widgets()

    def create_widgets(self):
        top = Frame(self)
        top.pack(pady=2)
        entry_frame = Frame(top)
        entry_frame.pack(side=LEFT)

        self.ent1 = Entry(entry_frame, width=10)
        self.ent1.pack()
        self.ent1.focus()

        self.ent2 = Entry(entry_frame, width=10)
        self.ent2.pack()

        self.btn = Button(top, text="Change")
        self.btn.pack(expand=1, padx=2)
        self.btn.bind('<Button-1>', self.resize)
        self.btn.bind('<Return>', self.resize)

        self.tb = Text(self, bg='lightgrey', width=20, height=10)
        self.tb.pack(pady=2)
        self.tb.bind('<FocusIn>', lambda event, color='white': self.focus_widget_text(event, color))
        self.tb.bind('<FocusOut>', lambda event, color='lightgrey': self.focus_widget_text(event, color))

    def resize(self, event):
        self.tb.config(width=int(self.ent1.get()), height=int(self.ent2.get())/2)

    def focus_widget_text(self, event, color):
        self.tb["bg"] = color

 
root = Tk()
root.title("Events")
root.minsize(205, 230)
app = App(root)
root.mainloop()