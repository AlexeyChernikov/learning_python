from tkinter import *


class App(Frame):
    __dishes = {
        "Onion soup": 100,
        "Caesar salad": 200,
        "Pizza": 300,
        "BBQ ribs": 400,
        "Grilled vegetables": 500,
        "Pancakes": 600,
        "Cherry pie": 700,
        "Vanilla pudding": 800,
        "Cheese sticks": 900,
        "Spaghetti Bolognese": 1000
    }

    def __init__(self, master):
        super(App, self).__init__(master)
        self.pack()
        self.__total_price = 0
        self.__create_widgets()

    def __create_widgets(self):
        # Menu
        menu_frame = LabelFrame(self, text="Menu")
        menu_frame.grid(row=0, padx=2, pady=2)
        self.__create_checkbtns(menu_frame)

        # Total price
        self.total_price_lbl = Label(self, text=f"Total price: ${self.__total_price}")
        self.total_price_lbl.grid(row=1, padx=2, pady=2, sticky=W)

        # Buttons
        btns_frame = Frame(self)
        btns_frame.grid(row=2, pady=2)

        Button(btns_frame, text="Check, please", command=self.__calculate).grid(padx=5)
        Button(btns_frame, text="Clear order", command=self.__refresh).grid(row=0, column=1, padx=5)

    def __calculate(self):
        self.__total_price = 0
        food_prices = [price for price in App.__dishes.values()]
        
        i = 0
        for _ in self.__ch:
            if self.__ch[i].get():
                self.__total_price += food_prices[i]
            i += 1

        self.total_price_lbl.config(text=f"Total price: ${self.__total_price}")

    def __refresh(self):
        i = 0
        for _ in self.__ch:
            self.__ch[i].set(False)
            i += 1

        self.__total_price = 0
        self.total_price_lbl.config(text=f"Total price: ${self.__total_price}")

    def __create_checkbtns(self, frame):
        half_dishes = None

        if len(App.__dishes) % 2 == 0:
            half_dishes = len(App.__dishes) // 2
        else:
            half_dishes = len(App.__dishes) // 2 + 1
        
        self.__ch = []
        i = 0
        _row = 0
        _col = 0

        for k, v in App.__dishes.items():
            if i == half_dishes:
                _row = 0
                _col = 2

            ch = BooleanVar()
            self.__ch.append(ch)
            Checkbutton(frame, text=k, variable=ch).grid(row=_row, column=_col, sticky=W)
            Label(frame, text=f"${v}").grid(row=_row, column=_col+1, sticky=W)
            
            _row += 1
            i += 1


def main():
    root = Tk()
    root.title("Check, please!")
    root.resizable(False, False)
    App(root)
    root.mainloop()


main()