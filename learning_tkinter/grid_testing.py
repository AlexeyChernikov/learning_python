from tkinter import *
from tkinter.ttk import Combobox


class CoordsWin(Frame):
    shape_colors = ('red', 'green', 'blue', 'black', 'white')

    def __init__(self, master):
        super(CoordsWin, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # Shape coords
        coords_frame = Frame(self)
        coords_frame.grid(row=0)

        ## X1
        Label(coords_frame, text="x1").grid(row=0, column=0)
        self.x1_ent = Entry(coords_frame)
        self.x1_ent.insert(END, "10")
        self.x1_ent.grid(row=0, column=1, columnspan=2)

        ## Y1
        Label(coords_frame, text="y1").grid(row=0, column=3)
        self.y1_ent = Entry(coords_frame)
        self.y1_ent.insert(END, "10")
        self.y1_ent.grid(row=0, column=4, columnspan=2)

        ## X2
        Label(coords_frame, text="x2").grid(row=1, column=0)
        self.x2_ent = Entry(coords_frame)
        self.x2_ent.insert(END, "50")
        self.x2_ent.grid(row=1, column=1, columnspan=2)
        
        ## Y2
        Label(coords_frame, text="y2").grid(row=1, column=3)
        self.y2_ent = Entry(coords_frame)
        self.y2_ent.insert(END, "50")
        self.y2_ent.grid(row=1, column=4, columnspan=2)

        # Figure selection rb
        rb_frame = Frame(self)
        rb_frame.grid(row=1)

        self.rb_var = IntVar()
        Radiobutton(rb_frame, text="Rectangle", variable=self.rb_var, value=0).grid(row=0, column=1, columnspan=2)
        Radiobutton(rb_frame, text="Circle", variable=self.rb_var, value=1).grid(row=0, column=3, columnspan=2)

        # Choice of color of a figure cb
        color_frame = Frame(self)
        color_frame.grid(row=2)

        Label(color_frame, text="Fill color").grid(row=0, column=1, sticky=W)
        self.fill_color = Combobox(color_frame, values=CoordsWin.shape_colors)
        self.fill_color.current(4)
        self.fill_color.grid(row=1, column=1, columnspan=2)

        Label(color_frame, text="Border color").grid(row=2, column=1, sticky=W)
        self.outline_color = Combobox(color_frame, values=CoordsWin.shape_colors)
        self.outline_color.current(3)
        self.outline_color.grid(row=3, column=1, columnspan=2)

        # Draw shape btn
        Button(self, text="Draw", font=24, width=20, bg='lightgray').grid(row=3, pady=3)


root = Tk()
root.title("Add shape")
root.resizable(False, False)
app = CoordsWin(root)
root.mainloop()