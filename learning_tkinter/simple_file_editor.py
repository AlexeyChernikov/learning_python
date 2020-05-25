from tkinter import *


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.pack()
        self.create_wigets()
        
    def create_wigets(self):
        top = Frame(self)
        top.pack()
        bottom = Frame(self)
        bottom.pack(padx=2, pady=1)
        text_frame = Frame(bottom)
        text_frame.pack()

        # Field with path
        self.path_entry = Entry(top, width=50)
        self.path_entry.pack(side=LEFT, padx=1, pady=1)

        # Open file button
        self.open_btn = Button(top, text="Open", command=self.open_file)
        self.open_btn.pack(side=LEFT, padx=1, pady=1)

        # Save file button
        self.save_btn = Button(top, text="Save", command=self.save_file)
        self.save_btn.pack(side=LEFT, padx=1, pady=1)

        # Edit field
        self.text = Text(text_frame, width=50, height=20, wrap=NONE)
        self.text.pack(side=LEFT)

        # Y scroll
        self.text_yscroll = Scrollbar(text_frame, command=self.text.yview)
        self.text_yscroll.pack(side=RIGHT, fill=Y)

        # X scroll
        self.text_xscroll = Scrollbar(bottom, orient=HORIZONTAL, command=self.text.xview)
        self.text_xscroll.pack(side=BOTTOM, fill=X)

        self.text.config(xscrollcommand=self.text_xscroll.set, yscrollcommand=self.text_yscroll.set)

    def open_file(self):
        self.text.delete(1.0, END)
        
        try:
            f = open(self.path_entry.get(), 'r')
            self.text.insert(INSERT, f.read())
        except FileNotFoundError:
            self.text.insert(INSERT, "File not found!")
        else:
            f.close()

    def save_file(self):
        try:
            f = open(self.path_entry.get(), 'w')
            f.write(self.text.get(1.0, END))
        except:
            self.text.insert(INSERT, "An error has occurred!")
        else:
            f.close()


root = Tk()
root.title("Simple file editor")
root.resizable(False, False)

app = Application(root)

root.mainloop()