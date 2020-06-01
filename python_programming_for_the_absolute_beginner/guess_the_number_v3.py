# Guess the number
#
# The computer selects a random number in the range from 1 to 100.
# The player is trying to guess this number.
# The computer says the assumption is more / less than the guessed number or hit the point.
# The player has only 10 attempts to guess the number

import random
from tkinter import *


class App(Frame):
    __intro = """Welcome to "Guess the Number"!\nI made up a natural number from 1 to 100.\nYou have only 10 attempts.\nLet's go!"""

    def __init__(self, master):
        super(App, self).__init__(master)
        self.pack()
        self.__create_widgets()
        self.__new_game()

    def __create_widgets(self):
        # Intro
        Label(self, text=App.__intro, justify=LEFT).grid(sticky=W)

        # Attempts
        self.__attempt_lbl = Label(self)
        self.__attempt_lbl.grid(row=1, sticky=W, pady=5)

        # Assumption
        self.__answer = Entry(self)
        self.__answer.grid(row=2, sticky=W + E)
        self.__answer.focus()
        
        # Result
        self.__result_lbl = Label(self)
        self.__result_lbl.grid(row=3, sticky=W, pady=5)

        # Buttons
        btns_frame = Frame(self)
        btns_frame.grid(row=4)

        Button(btns_frame, text="Guess", command=self.__guess).grid(row=0, padx=2)
        Button(btns_frame, text="Restart", command=self.__new_game).grid(row=0, column=1, padx=2)

    def __new_game(self):
        self.__guessed_number = random.randint(1, 100)
        self.__attempts_counter = 10
        self.__assumption = None
        self.__result = True

        self.__attempt_lbl.config(text=f"Attempts left: {self.__attempts_counter}")
        self.__answer.delete(0, END)
        self.__result_lbl.config(text="Result: Enter the number")

    def __input_check(self):
        if self.__answer.get().isdigit():
            self.__assumption = int(self.__answer.get())
            return True
        else:
            self.__result_lbl.config(text="Result: Enter the number")
            self.__answer.delete(0, END)
            return False
    
    def __guess(self):
        if self.__result:
            if self.__input_check():
                self.__attempts_counter -= 1
                self.__attempt_lbl.config(text=f"Attempts left: {self.__attempts_counter}")

                if self.__assumption == self.__guessed_number:
                    self.__result_lbl.config(text="Result: You guessed!")
                    self.__result = False
                elif (self.__assumption != self.__guessed_number) and (self.__attempts_counter == 0):
                    self.__result_lbl.config(text="Result: You did not guess!")
                    self.__result = False
                elif self.__assumption > self.__guessed_number:
                    self.__result_lbl.config(text="Result: Less...")
                elif self.__assumption < self.__guessed_number:
                    self.__result_lbl.config(text="Result: More...")
        else:
            self.__new_game()


def main():
    win_width = 270
    win_height = 180

    root = Tk()
    root.title("Guess the number")

    center_screen_coords = (root.winfo_screenwidth() // 2 - win_width // 2, root.winfo_screenheight() // 2 - win_height // 2)
    
    root.geometry(f"{win_width}x{win_height}+{center_screen_coords[0]}+{center_screen_coords[1]}")
    root.resizable(False, False)
    App(root)
    root.mainloop()


main()