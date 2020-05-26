from tkinter import *


class App(Frame):
    languages = [("Python", 0), ("C#", 1), ("C++", 2), ("Java", 3), ("JavaScript", 4)]

    def __init__(self, master):
        super(App, self).__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text="Choose language:").pack()

        self.rb_frame = Frame(self)
        self.rb_frame.pack()

        self.rb_var = IntVar()
        for lang, val in App.languages:
            Radiobutton(self.rb_frame, text=lang, variable=self.rb_var, value=val, command=self.select).pack(side=LEFT)

        self.selected = Label(self, text="Selected language:")
        self.selected.pack()

    def select(self):
        var = self.rb_var.get()
        
        if var == 0:
            self.selected.config(text=f"Selected language: {App.languages[0][0]}")
        elif var == 1:
            self.selected.config(text=f"Selected language: {App.languages[1][0]}")
        elif var == 2:
            self.selected.config(text=f"Selected language: {App.languages[2][0]}")
        elif var == 3:
            self.selected.config(text=f"Selected language: {App.languages[3][0]}")
        elif var == 4:
            self.selected.config(text=f"Selected language: {App.languages[4][0]}")


root = Tk()
root.title("Radiobuttons")

app = App(root)

root.mainloop()