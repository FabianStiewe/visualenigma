import tkinter as tk

from visualenigma.stripe import Stripe

class ReflectorDisplay(tk.Frame):

    def __init__(self, box_int, **kwargs):
        self.box_int = box_int
        super().__init__(master=box_int, bg=self.box_int.gui.color_scheme['global_bg'], **kwargs)
        self.contacts_style = 1
        self.cor_contacts_style = 1
        self.make()
        self.update()

    def make(self):

        dummy = ['' for i in range(self.box_int.gui.machine.length)]

        self.contacts = Stripe(self, dummy)

        self.contacts.grid(row=0, column=5)

        self.corresponding_contacts = Stripe(self, dummy)

        self.corresponding_contacts.grid(row=0, column=0)


    def update(self):

        # contacts

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
            fg=self.box_int.gui.color_scheme['reflector_fg'],
            bg=self.box_int.gui.color_scheme['reflector_bg']
            )
        self.contacts.squares[0].configure(
            fg=self.box_int.gui.color_scheme['reflector_zero_fg'],
            bg=self.box_int.gui.color_scheme['reflector_zero_bg']
            )

        # corresponding contacts

        if self.cor_contacts_style == 0:
            export = [self.box_int.gui.machine.box.reflector.wiring[i]
                      for i in range(self.box_int.gui.machine.length)]
        elif self.cor_contacts_style == 1:
            export = [self.box_int.gui.machine.alphabet[
                      self.box_int.gui.machine.box.reflector.wiring[i]
                      ]
                      for i in range(self.box_int.gui.machine.length)]
        elif self.cor_contacts_style == 2:
            export = [self.box_int.gui.machine.numberline[
                      self.box_int.gui.machine.box.reflector.wiring[i]
                      ]
                      for i in range(self.box_int.gui.machine.length)]
        elif self.cor_contacts_style == 3:
            export = ['' for i in range(self.box_int.gui.machine.length)]
        self.corresponding_contacts.configure(
            symbols=export,
            fg=self.box_int.gui.color_scheme['c_reflector_fg'],
            bg=self.box_int.gui.color_scheme['c_reflector_bg']
            )
        self.corresponding_contacts.squares[0].configure(
            fg=self.box_int.gui.color_scheme['c_reflector_zero_fg'],
            bg=self.box_int.gui.color_scheme['c_reflector_zero_bg']
            )
