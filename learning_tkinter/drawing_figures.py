from tkinter import *
from tkinter.ttk import Combobox


class App(Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.canv = Canvas(root, background="white")
        self.canv.pack()

        Button(root, text="Add shape", command=self.create_add_shape_window).pack()

    def create_add_shape_window(self):
        # Window
        add_shape_win = Toplevel()
        add_shape_win.title("Add shape")
        add_shape_win.geometry(f"+{int(root.winfo_screenwidth()//2+win_width//2+1)}+{int(root.winfo_screenheight()//2-win_height//2)}")
        add_shape_win.resizable(False, False)
        add_shape_win.focus_set()
        self.app = CoordsWin(add_shape_win, self.canv)


class CoordsWin(Frame):
    shape_colors = ('red', 'green', 'blue', 'black', 'white')

    def __init__(self, master, canv):
        super(CoordsWin, self).__init__(master)
        self.pack()
        self.canv = canv
        self.create_widgets()

    def create_widgets(self):
        # Shape coords
        coords_frame = Frame(self)
        coords_frame.pack()

        top_coords_frame = Frame(coords_frame)
        top_coords_frame.pack()

        bottom_coords_frame = Frame(coords_frame)
        bottom_coords_frame.pack()

        ## X1
        Label(top_coords_frame, text="x1").pack(side=LEFT)
        self.x1_ent = Entry(top_coords_frame)
        self.x1_ent.insert(END, "10")
        self.x1_ent.pack(side=LEFT)

        ## Y1
        Label(top_coords_frame, text="y1").pack(side=LEFT)
        self.y1_ent = Entry(top_coords_frame)
        self.y1_ent.insert(END, "10")
        self.y1_ent.pack(side=LEFT)

        ## X2
        Label(bottom_coords_frame, text="x2").pack(side=LEFT)
        self.x2_ent = Entry(bottom_coords_frame)
        self.x2_ent.insert(END, "50")
        self.x2_ent.pack(side=LEFT)
        
        ## Y2
        Label(bottom_coords_frame, text="y2").pack(side=LEFT)
        self.y2_ent = Entry(bottom_coords_frame)
        self.y2_ent.insert(END, "50")
        self.y2_ent.pack(side=LEFT)

        # Figure selection rb
        rb_frame = Frame(self)
        rb_frame.pack()

        self.rb_var = IntVar()
        Radiobutton(rb_frame, text="Rectangle", variable=self.rb_var, value=0).pack(side=LEFT)
        Radiobutton(rb_frame, text="Circle", variable=self.rb_var, value=1).pack(side=LEFT)

        # Choice of color of a figure cb
        color_frame = Frame(self)
        color_frame.pack()

        Label(color_frame, text="Fill color").pack(anchor=W)
        self.fill_color = Combobox(color_frame, values=CoordsWin.shape_colors)
        self.fill_color.current(4)
        self.fill_color.pack(anchor=W)

        Label(color_frame, text="Border color").pack(anchor=W)
        self.outline_color = Combobox(color_frame, values=CoordsWin.shape_colors)
        self.outline_color.current(3)
        self.outline_color.pack(anchor=W)

        # Draw shape btn
        Button(self, text="Draw", command=self.draw_shape, font=24, width=20, bg='lightgray').pack(pady=3)

    def draw_shape(self):
        if self.rb_var.get() == 0:
            self.draw_rect()
        elif self.rb_var.get() == 1:
            self.draw_circle()

    def draw_rect(self):
        self.canv.create_rectangle(
            self.x1_ent.get(),
            self.y1_ent.get(),
            self.x2_ent.get(),
            self.y2_ent.get(),
            fill=self.fill_color.get(),
            outline=self.outline_color.get()
            )

    def draw_circle(self):
        self.canv.create_oval(
            self.x1_ent.get(),
            self.y1_ent.get(),
            self.x2_ent.get(),
            self.y2_ent.get(),
            fill=self.fill_color.get(),
            outline=self.outline_color.get()
            )


win_width = 400
win_height = 300

root = Tk()
root.title("Canvas")
root.geometry(f"{win_width}x{win_height}+{int(root.winfo_screenwidth()//2-win_width//2)}+{int(root.winfo_screenheight()//2-win_height//2)}")
root.resizable(False, False)
app = App(root)
root.mainloop()