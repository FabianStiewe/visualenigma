=============
Visual Enigma
=============

Visual Enigma provides a graphic simulation of the famous Enigma machine
and similar cryptographic rotor machines.

import tkinter as tk
import visualenigma.machine as vem

root = tk.Tk()
my_machine = vem.CipheringMachine(root,
                                  rotor_set=(ROTOR_VI, ROTOR_VIII, ROTOR_V),
                                  reflector=UKW_B)
root.mainloop()
