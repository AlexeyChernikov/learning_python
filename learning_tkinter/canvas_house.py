from tkinter import *

root = Tk()
root.resizable(False, False)

canv = Canvas(root, width=300, height=270, background="white")
canv.pack()

# Sun
canv.create_oval((240, 10), (290, 60), fill='orange', outline='orange')

# House
canv.create_polygon(
    (150, 50),  # Roof top
    (240, 110), # Lower right corner of the roof
    (215, 110), # Upper right corner of the wall
    (215, 230), # Lower right corner of the wall
    (75, 230),  # Lower left corner of the wall
    (75, 110),  # Upper left corner of the wall
    (50, 110),  # Lower left corner of the roof
    fill='lightblue',
    outline='lightblue'
    )

# Alternative house
# canv.create_line(150, 230, 150, 50, fill='lightblue', width=140, arrow=LAST, arrowshape="60 60 25")

# Grass
for i in range(-40, 300, 12):
    canv.create_arc(i, 180, (350+i), 360, start=180, extent=-35, style=ARC, outline='green', width=3)

root.mainloop()