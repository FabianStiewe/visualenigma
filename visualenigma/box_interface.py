import tkinter as tk

from visualenigma.plugboard_display import PlugboardDisplay
from visualenigma.entry_stator_display import EntryStatorDisplay
from visualenigma.rotor_display import RotorDisplay
from visualenigma.reflector_display import ReflectorDisplay

class BoxInterface(tk.Frame):

    def __init__(self, gui):
        self.gui = gui
        super().__init__(master=gui,
                         bg=self.gui.color_scheme['global_bg'],
                         padx=20, pady=20)
        self.make()
        print('        Rotors interface initialized successfully.')

    def make(self):
        self.plugboard_disp = PlugboardDisplay(self, padx=20)
        self.plugboard_disp.grid(row=0,
                                 column=2+len(self.gui.machine.box.rotors))
        self.entry_stator_disp = EntryStatorDisplay(self, padx=20)
        self.entry_stator_disp.grid(row=0,
                                    column=1+len(self.gui.machine.box.rotors))
        self.rotors_disp = []
        for i in range(len(self.gui.machine.box.rotors)):
            self.rotors_disp.append(RotorDisplay(self, i, padx=20))
            self.rotors_disp[i].grid(row=0, column=i+1)
        self.reflector_disp = ReflectorDisplay(self, padx=20)
        self.reflector_disp.grid(row=0, column=0)

    def update_rotors(self):
        for rotor in self.rotors_disp:
            rotor.update()

    def update_all(self):
        self.plugboard_disp.update()
        self.entry_stator_disp.update()
        self.update_rotors()
        self.reflector_disp.update()
