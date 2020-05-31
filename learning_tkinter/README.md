# Exploring the Tkinter library:
## List of written programs:
### 1. Rainbow of buttons:
**Description:** Write a program consisting of seven buttons whose colors correspond to the colors of the rainbow. When a button is clicked, the color code must be inserted in the text field, and the color name must be inserted in the label. Color codes in hexadecimal encoding: #ff0000-red, #ff7d00-orange, #ffff00 – yellow, #00ff00 – green, #007dff – light blue, #0000ff – blue, #7d00ff – purple.

**Code:** [rainbow_of_btns.py](./rainbow_of_btns.py)

### 2. Rainbow of buttons (using the parameters of the pack() method):
**Description:** Modify the code of the previous program using the parameters of the pack() method.

**Code:** [rainbow_of_btns_v2.py](./rainbow_of_btns_v2.py)

### 3. Simple file editor:
**Description:** Write a program consisting of single-line and multi-line text fields and two "Open" and "Save" buttons. When you click on the first one, a file should be opened for reading, whose name is indicated in the field of the Entry class, and the contents of the file should be loaded into the field of type Text.

When you click on the second button, the text entered by the user in the Text instance should be saved in a file under the name that the user specified in the single-line text field.

Files will be read and written in the same directory as the script file, if you specify file names without an address.

**Code:** [simple_file_editor.py](./simple_file_editor.py)

### 4. Radiobuttons:
**Description:** Write a program that has several radio buttons grouped together. If a button is enabled, the label should display the corresponding information.

**Code:** [radiobuttons.py](./radiobuttons.py)

### 5. Shopping list:
**Description:** Write a program consisting of two Listbox lists. The first will be, for example, a list of goods specified programmatically. The second is initially empty, let it be a shopping list. When you click on one button, the product should go from one list to another. When you click on the second button - return (the person changed his mind to buy). Provide for multiple selection of list items and their movement.

**Code:** [shopping_list.py](./shopping_list.py)

### 6. Method bind():
**Description:** Write the program as follows. Pressing Enter in a single-line text field moves the text from it to the list. If you double-click on the list item, it should be copied to the text box.

**Code:** [method_bind.py](./method_bind.py)

### 7. Events:
**Description:** Write the program according to the description. The dimensions of a multi-line text field are determined by the values entered in single-line text fields. The size changes when the mouse clicks on the button, as well as when the Enter key is pressed. The background color of the Text instance is light grey when the field is out of focus, and white when it has focus.

**Code:** [events.py](./events.py)

### 8. Canvas house:
**Description:** Draw a house, sun and grass using Canvas.

**Code:** [canvas_house.py](./canvas_house.py)

### 9. Canvas animation:
**Description:** Program the gradual movement of the figure to the point on the canvas where the user clicks with the left mouse button.

**Code:** [canvas_animation.py](./canvas_animation.py)

### 10. Drawing figures:
**Description:** Write a program that has a canvas and a "Add shape" button on the main window. The button opens a second window that includes four fields for entering coordinates and two radio buttons for choosing whether to draw a rectangle or an oval on the canvas. Here you can also find the "Draw" button, when you click on it, the corresponding shape is added to the canvas, and the second window closes. You can omit checking for correct input in the fields.

**Code:** [drawing_figures.py](./drawing_figures.py)

### 11. Grid testing:
**Description:** Reprogram the second window from job 10 (Drawing figures) using the grid() method.

**Code:** [grid_testing.py](./grid_testing.py)

### 12. Dialog windows:
**Description:** Make a simple file editor with using dialog windows.

**Code:** [simple_file_editor_with_dw.py](./simple_file_editor_with_dw.py)