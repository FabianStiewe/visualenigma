import tkinter as tk

class Stripe(tk.Frame):

    """A single column of numbers or letters to display in the box interface."""

    def __init__(self, box_int, symbols,
                 fg='black', bg='white', relief=tk.FLAT):
        self.box_int = box_int
        super().__init__(master=self.box_int)

        self.symbols = symbols
        self.length = len(self.symbols)
        self.squares = []

        for i in range(self.length):
            square = tk.Label(master=self, text=self.symbols[i],
                              width=2, height=1,
                              fg=fg, bg=bg,
                              bd=2, relief=relief)
            self.squares.append(square)
            square.grid(row=((self.length - 1)//2 - i)%self.length, column=0)

    def configure(self, symbols, **kwargs):
        if len(symbols) != self.length:
            print('Cannot change stripe length.')
        else:
            for i in range(self.length):
                self.squares[i].configure(text=symbols[i], **kwargs)
