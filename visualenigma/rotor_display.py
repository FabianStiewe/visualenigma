import tkinter as tk

from visualenigma.stripe import Stripe
from visualenigma.utils import empty_string_list, update_component, update_notches, update_ring_position

class RotorDisplay(tk.Frame):

    def __init__(self, box_int, rotor_number, **kwargs):
        self.box_int = box_int
        super().__init__(master=box_int, bg=self.box_int.gui.color_scheme['global_bg'], **kwargs)
        self.number = rotor_number
        self.dummy = tuple(['' for i in range(self.box_int.gui.machine.length)])
        self.ring_style = 1
        self.pin_style = 2
        self.flat_style = 2
        self.cor_pin_style = 2
        self.cor_flat_style = 2
        self.make()
        self.update()
        self.notches.grid(row=0, column=0)
        self.ring.grid(row=0, column=1)
        self.ring_position.grid(row=0, column=2)
        self.pins.grid(row=0, column=6)
        self.flats.grid(row=0, column=3)
        self.corresponding_pins.grid(row=0, column=4)
        self.corresponding_flats.grid(row=0, column=5)

    def make(self):

        self.ring = Stripe(self, self.dummy, relief=tk.RAISED)   

        self.pins = Stripe(self, self.dummy)

        self.flats = Stripe(self, self.dummy)

        self.corresponding_pins = Stripe(self, self.dummy)

        self.corresponding_flats = Stripe(self, self.dummy)

        self.notches = Stripe(self, self.dummy)
       
        self.ring_position = Stripe(self, self.dummy)

    def update(self):

        # ring

        func = lambda i, rotors, n, length: (i + rotors[n].window_letter) % length

        update_component(self.box_int.gui.machine,
                         self.box_int.gui.color_scheme,
                         self.ring,
                         self.ring_style,
                         'ring',
                         self.number,
                         func)

        # pins

        func = lambda i, rotors, n, length: (i - rotors[n].zero) % length

        update_component(self.box_int.gui.machine,
                         self.box_int.gui.color_scheme,
                         self.pins,
                         self.pin_style,
                         'pin',
                         self.number,
                         func)

        # flats

        func = lambda i, rotors, n, length: (i - rotors[n].zero) % length

        update_component(self.box_int.gui.machine,
                         self.box_int.gui.color_scheme,            
                         self.flats,
                         self.flat_style,
                         'flat',
                         self.number,
                         func)

        # corresponding pins

        func = lambda i, rotors, n, length: rotors[n].pins[(i - rotors[n].zero) % length]

        update_component(self.box_int.gui.machine,
                         self.box_int.gui.color_scheme,
                         self.corresponding_pins,
                         self.cor_pin_style,
                         'c_pin',
                         self.number,
                         func)        

        # corresponding flats

        func = lambda i, rotors, n, length: rotors[n].flats[(i - rotors[n].zero) % length]

        update_component(self.box_int.gui.machine,
                         self.box_int.gui.color_scheme,            
                         self.corresponding_flats,
                         self.cor_flat_style,
                         'c_flat',
                         self.number,
                         func) 

        # notches

        update_notches(self.box_int.gui.machine,
                       self.box_int.gui.color_scheme,            
                       self.notches,
                       self.dummy,
                       self.number)

        # ring position

        update_ring_position(self.box_int.gui.machine,
                             self.box_int.gui.color_scheme,            
                             self.ring_position,
                             self.dummy,
                             self.number)