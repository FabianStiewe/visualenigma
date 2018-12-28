import tkinter as tk

from visualenigma.stripe import Stripe

class PlugboardDisplay(tk.Frame):

    def __init__(self, box_int, **kwargs):
        self.box_int = box_int
        super().__init__(master=box_int,
                         bg=self.box_int.gui.color_scheme['global_bg'],
                         **kwargs) 
        self.kb_contacts_style = 1
        self.es_contacts_style = 1
        self.cor_kb_contacts_style = 1
        self.cor_es_contacts_style = 1
        self.make()
        self.update()

    def make(self):
        dummy = ['' for i in range(self.box_int.gui.machine.length)]
        self.key_contacts = Stripe(self, dummy)
        self.stator_contacts = Stripe(self, dummy)
        self.stator_contacts.grid(row=0, column=0)
        self.key_contacts.grid(row=0, column=3)
        self.corresponding_key_contacts = Stripe(self, dummy)
        self.corresponding_stator_contacts = Stripe(self, dummy)
        self.corresponding_stator_contacts.grid(row=0, column=2)
        self.corresponding_key_contacts.grid(row=0, column=1)

    def update(self):
        # Contacts connected to keyboard
        if self.kb_contacts_style == 0:
            export = range(self.box_int.gui.machine.length)
        elif self.kb_contacts_style == 1:
            export = self.box_int.gui.machine.alphabet
        elif self.kb_contacts_style == 2:
            export = self.box_int.gui.machine.numberline
        elif self.kb_contacts_style == 3:
            export = ['' for i in range(self.box_int.gui.machine.length)]
        self.key_contacts.configure(
            symbols=export,
            fg=self.box_int.gui.color_scheme['plug_key_fg'],
            bg=self.box_int.gui.color_scheme['plug_key_bg']
            )
        self.key_contacts.squares[0].configure(
            fg=self.box_int.gui.color_scheme['plug_key_zero_fg'],
            bg=self.box_int.gui.color_scheme['plug_key_zero_bg']
            )
        # Corresponding entry-stator-side contacts
        if self.cor_es_contacts_style == 0:
            export = [self.box_int.gui.machine.box.plugboard.wiring[i]
                      for i in range(self.box_int.gui.machine.length)]
        elif self.cor_es_contacts_style == 1:
            export = [self.box_int.gui.machine.alphabet[
                      self.box_int.gui.machine.box.plugboard.wiring[i]
                      ]
                      for i in range(self.box_int.gui.machine.length)]
        elif self.cor_es_contacts_style == 2:
            export = [self.box_int.gui.machine.numberline[
                      self.box_int.gui.machine.box.plugboard.wiring[i]
                      ]
                      for i in range(self.box_int.gui.machine.length)]
        elif self.cor_es_contacts_style == 3:
            export = ['' for i in range(self.box_int.gui.machine.length)]
        self.corresponding_stator_contacts.configure(
            symbols=export,
            fg=self.box_int.gui.color_scheme['plug_c_stator_fg'],
            bg=self.box_int.gui.color_scheme['plug_c_stator_bg']
            )
        self.corresponding_stator_contacts.squares[0].configure(
            fg=self.box_int.gui.color_scheme['plug_c_stator_zero_fg'],
            bg=self.box_int.gui.color_scheme['plug_c_stator_zero_bg']
            )
        # Contacts connected to entry stator
        if self.es_contacts_style == 0:
            export = range(self.box_int.gui.machine.length)
        elif self.es_contacts_style == 1:
            export = self.box_int.gui.machine.alphabet
        elif self.es_contacts_style == 2:
            export = self.box_int.gui.machine.numberline
        elif self.es_contacts_style == 3:
            export = ['' for i in range(self.box_int.gui.machine.length)]
        self.stator_contacts.configure(
            symbols=export,
            fg=self.box_int.gui.color_scheme['plug_stator_fg'],
            bg=self.box_int.gui.color_scheme['plug_stator_bg']
            )
        self.stator_contacts.squares[0].configure(
            fg=self.box_int.gui.color_scheme['plug_stator_zero_fg'],
            bg=self.box_int.gui.color_scheme['plug_stator_zero_bg']
            )
        # Corresponding keyboard-side contacts
        if self.cor_kb_contacts_style == 0:
            export = [self.box_int.gui.machine.box.plugboard.wiring[i]
                      for i in range(self.box_int.gui.machine.length)]
        elif self.cor_kb_contacts_style == 1:
            export = [self.box_int.gui.machine.alphabet[
                      self.box_int.gui.machine.box.plugboard.wiring[i]
                      ]
                      for i in range(self.box_int.gui.machine.length)]
        elif self.cor_kb_contacts_style == 2:
            export = [self.box_int.gui.machine.numberline[
                      self.box_int.gui.machine.box.plugboard.wiring[i]
                      ]
                      for i in range(self.box_int.gui.machine.length)]
        elif self.cor_kb_contacts_style == 3:
            export = ['' for i in range(self.box_int.gui.machine.length)]
        self.corresponding_key_contacts.configure(
            symbols=export,
            fg=self.box_int.gui.color_scheme['plug_c_key_fg'],
            bg=self.box_int.gui.color_scheme['plug_c_key_bg']
            )
        self.corresponding_key_contacts.squares[0].configure(
            fg=self.box_int.gui.color_scheme['plug_c_key_zero_fg'],
            bg=self.box_int.gui.color_scheme['plug_c_key_zero_bg']
            )




