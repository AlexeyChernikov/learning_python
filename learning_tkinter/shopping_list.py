from tkinter import *


class App(Frame):
    products = [
        'carrot', 'tomato', 'paper', 'pen', 'glass',
        'meat', 'banana', 'elephant', 'bird', 'beer',
        'water', 'computer', 'python', 'ballon', 'bag'
        ]

    def __init__(self, master):
        super(App, self).__init__(master)
        self.pack(padx=2, pady=2)
        self.create_widgets()

    def create_widgets(self):
        # Products list
        products_frame = Frame(self)
        products_frame.pack(side=LEFT)

        self.products_list = Listbox(products_frame, selectmode=EXTENDED)
        for item in App.products:
            self.products_list.insert(END, item)
        
        self.products_list.pack(side=LEFT)

        products_list_yscroll = Scrollbar(products_frame, command=self.products_list.yview)
        products_list_yscroll.pack(side=LEFT, fill=Y)

        self.products_list.config(yscrollcommand=products_list_yscroll)

        # Transfer buttons
        buttons = Frame(self)
        buttons.pack(side=LEFT, padx=2)

        Button(buttons, text=">>>", command=self.right_click).pack(pady=1)
        Button(buttons, text="<<<", command=self.left_click).pack(pady=1)

        # Purchases list
        purchases_frame = Frame(self)
        purchases_frame.pack(side=LEFT)

        self.purchases_list = Listbox(purchases_frame, selectmode=EXTENDED)
        self.purchases_list.pack(side=LEFT)

        purchases_list_yscroll = Scrollbar(purchases_frame, command=self.purchases_list.yview)
        purchases_list_yscroll.pack(side=LEFT, fill=Y)

        self.purchases_list.config(yscrollcommand=purchases_list_yscroll)

    def right_click(self):
        """ From the left list to the right list """
        self.__move_items(self.products_list, self.purchases_list)

    def left_click(self):
        """ From the right list to the left list """
        self.__move_items(self.purchases_list, self.products_list)

    def __move_items(self, cur_list, transfer_list):
        selected_items = list(cur_list.curselection())

        # Add selected items
        for item in selected_items:
            transfer_list.insert(END, cur_list.get(item))

        # Delete selected items
        selected_items.reverse()
        for item in selected_items:
            cur_list.delete(item)


root = Tk()
root.title("Shopping list")
root.resizable(False, False)
app = App(root)
root.mainloop()