import tkinter as tk

from visualenigma.stripe import Stripe

class EntryStatorDisplay(tk.Frame):

    def __init__(self, box_int, **kwargs):
        self.box_int = box_int
        super().__init__(master=box_int,
                         bg=self.box_int.gui.color_scheme['global_bg'],
                         **kwargs)
        self.contacts_style = 2
        self.make()
        self.update()

    def make(self):
        dummy = ['' for i in range(self.box_int.gui.machine.length)]
        self.contacts = Stripe(self, dummy)
        self.contacts.grid(row=0, column=2)

    def update(self):
        # The contacts equal the square indices inside the Stripe.
        if self.contacts_style == 0:
            export = range(self.box_int.gui.machine.length)
        elif self.contacts_style == 1:
            export = self.box_int.gui.machine.alphabet
        elif self.contacts_style == 2:
            export = self.box_int.gui.machine.numberline
        elif self.contacts_style == 3:
            export = ['' for i in range(self.box_int.gui.machine.length)]
        self.contacts.configure(
            symbols=export,
            fg=self.box_int.gui.color_scheme['entry_fg'],
            bg=self.box_int.gui.color_scheme['entry_bg']
            )
        self.contacts.squares[0].configure(
            fg=self.box_int.gui.color_scheme['entry_zero_fg'],
            bg=self.box_int.gui.color_scheme['entry_zero_bg']
            )
