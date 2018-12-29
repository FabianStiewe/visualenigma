from sys import argv
import tkinter as tk

import visualenigma.machine as vem
import visualenigma.machine_data as md
from visualenigma.utils import create_random_rotor


root = tk.Tk()
root.title('Visual Enigma')

# Use command-line parameter to choose among different demos:

# 'Classic' Enigma
if len(argv) < 2:

    the_machine = vem.CipheringMachine(master=root)

# M4-type Enigma
elif argv[1] == 'M4':

    the_machine = vem.CipheringMachine(master=root,
                                       rotor_set=[md.ROTOR_BETA,
                                                  md.ROTOR_IV,
                                                  md.ROTOR_V,
                                                  md.ROTOR_VI],
                                       reflector=md.UKW_B_THIN,
                                       stepping_mode='M4')

# 3-rotor Enigma with random internal wiring of rotors and reflector
elif argv[1] == 'random':

    print('___________________________________________')
    print('Generating random rotors:')
    rotor1 = create_random_rotor(26, 1, 'Random 1')
    print(rotor1)
    rotor2 = create_random_rotor(26, 2, 'Random 2')
    print(rotor2)
    rotor3 = create_random_rotor(26, 1, 'Random 3')
    print(rotor3)
    ukw = create_random_rotor(26, 0, 'Random UKW')
    print(ukw)
    print('___________________________________________')

    the_machine = vem.CipheringMachine(master=root,
                                       rotor_set=[rotor1, rotor2, rotor3],
                                       reflector=ukw)

# 3-rotor Enigma with 6-letter alphabet and random internal wirings
elif argv[1] == 'enigma':

    print('___________________________________________')
    print('Generating random rotors:')
    rotor1 = create_random_rotor(6, 1, 'Random 1')
    print(rotor1)
    rotor2 = create_random_rotor(6, 1, 'Random 2')
    print(rotor2)
    rotor3 = create_random_rotor(6, 1, 'Random 3')
    print(rotor3)
    ukw = create_random_rotor(6, 0, 'Random UKW')
    print(ukw)
    print('___________________________________________')

    the_machine = vem.CipheringMachine(master=root,
                                       alphabet=md.ENIGMA_ALPHABET,
                                       rotor_set=[rotor1, rotor2, rotor3],
                                       reflector=ukw,
                                       prawl_position=2)

# 3-rotor Enigma with alphabet letters replaced by symbols
elif argv[1] == 'symbols':

    the_machine = vem.CipheringMachine(master=root,
                                       alphabet=md.SYMBOL_ALPHABET)

root.mainloop()
