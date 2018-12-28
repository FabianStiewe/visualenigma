import tkinter as tk

from visualenigma.keyboard_interface import KeyboardInterface
from visualenigma.lamppanel_interface import LampPanelInterface
from visualenigma.plugboard_interface import PlugboardInterface
from visualenigma.box_interface import BoxInterface
from visualenigma.controls_interface import ControlsInterface
from visualenigma.machine_data import DEFAULT_COLOR_SCHEME

class GUI(tk.Frame):

    def __init__(self, machine, root):
        super().__init__(master=root, bg=DEFAULT_COLOR_SCHEME['global_bg'])
        self.machine = machine
        self.color_scheme = DEFAULT_COLOR_SCHEME
        print('        Initializing controls interface...')
        self.controls_int = ControlsInterface(self)
        self.controls_int.grid(row=0, column=1)
        print('        Initializing keyboard interface...')
        self.keyboard_int = KeyboardInterface(self)
        self.keyboard_int.grid(row=2, column=1)
        print('        Initializing lamp panel interface...')
        self.lamppanel_int = LampPanelInterface(self)
        self.lamppanel_int.grid(row=1, column=1)
        print('        Initializing plugboard interface...')
        self.plugboard_int = PlugboardInterface(self)
        self.plugboard_int.grid(row=3, column=0)
        print('        Initializing box interface...')
        self.box_int = BoxInterface(self)
        self.box_int.grid(row=0, column=0, rowspan=3)
        self.grid()
        print('    GUI initialized successfully.')



    def visualize(self, letter):
        forw = self.color_scheme['signal_forward_bg']
        back = self.color_scheme['signal_backward_bg']

        # Switch off all lamps
        for j in range(len(self.machine.alphabet)):
            self.lamppanel_int.lamps[j].switch_off()
        print('Key pressed:                 {}'.format(letter))

        # Generate the iterator for sending the letter signal through the box
        crypterator = self.machine.box.process(letter)
        signal = next(crypterator)                         # Initial signal

        # Stepping of rotors
        next(crypterator)
        self.box_int.update_all()

        # Pass signal through plugboard
        self.box_int.plugboard_disp.key_contacts.squares[
            signal
            ].configure(bg=forw)            
        signal = next(crypterator)                         # After plugboard
        self.box_int.plugboard_disp.stator_contacts.squares[
            signal
            ].configure(bg=forw)

        # Pass signal through entry stator
        self.box_int.entry_stator_disp.contacts.squares[
            signal
            ].configure(bg=forw)

        # Pass signal through rotors right to left  
        for i in range(len(self.machine.box.rotors)):
            next(crypterator)                              # Enter rotor
            self.box_int.rotors_disp[-i-1].pins.squares[
                signal
                ].configure(bg=forw)
            signal = next(crypterator)                     # Pin
            signal = next(crypterator)                     # Flat
            signal = next(crypterator)                     # Exit
            self.box_int.rotors_disp[-i-1].flats.squares[
                signal
                ].configure(bg=forw)
            signal = next(crypterator)                     # After rotor

        # Pass signal through reflector
        self.box_int.reflector_disp.contacts.squares[
            signal
            ].configure(bg=forw)
        signal = next(crypterator)                         # After reflector
        self.box_int.reflector_disp.contacts.squares[
            signal
            ].configure(bg=back)

        # Pass signal through rotors left to right
        for i in range(len(self.machine.box.rotors)):
            next(crypterator)                              # Enter rotor
            self.box_int.rotors_disp[i].flats.squares[
                signal
                ].configure(bg=back)
            signal = next(crypterator)                     # Flat
            signal = next(crypterator)                     # Pin
            signal = next(crypterator)                     # Exit
            self.box_int.rotors_disp[i].pins.squares[
                signal
                ].configure(bg=back)
            signal = next(crypterator)                     # After rotor

        # Pass signal through entry stator
        self.box_int.entry_stator_disp.contacts.squares[
            signal
            ].configure(bg=back)

        # Pass signal through plugboard
        self.box_int.plugboard_disp.stator_contacts.squares[
            signal
            ].configure(bg=back)
        signal = next(crypterator)                         # After plugboard
        self.box_int.plugboard_disp.key_contacts.squares[
            signal
            ].configure(bg=back)
        signal = next(crypterator)                         # Encrypted letter

        print('Encrypted letter:            {}'.format(signal))

        # Switch on lamp for encrypted letter
        self.lamppanel_int.lamps[
            self.lamppanel_int.indices[signal]
            ].switch_on()
