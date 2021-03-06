import tkinter as tk

from visualenigma.plugboard import Plugboard
from visualenigma.stepping import SteppingMechanism
from visualenigma.rotor import Rotor
from visualenigma.reflector import Reflector

class Box():

    """The 'gearbox' containing the 'mechanics' of the machine.

    The box coordinates the movement (stepping) of the rotors and the
    processing of a signal (letter) through the plugboard, the rotors, the
    reflector and back."""
    
    def __init__(self, machine):
        self.machine = machine
        print('        Initializing plugboard...')
        self.plugboard = Plugboard(self)
        print('        Initializing stepping mechnaism...')
        self.stepping = SteppingMechanism(self)
        self.rotors = []
        for i in range(len(self.machine.rotor_set)):
            print('        Initializing rotor {}...'.format(i+1))
            self.rotors.append(Rotor(self, self.machine.rotor_set[i]))
        print('        Initializing reflector...')
        self.reflector = Reflector(self, self.machine.reflector)
        print('    Box initialized successfully.')

    def process(self, letter):
        # Translate letter into number (= the 'signal' to be processed)
        signal = self.machine.indices[letter]
        print('Initial signal:          {:2d}  {}  {}'.format(
            signal,
            self.machine.alphabet[signal],
            self.machine.numberline[signal]
            ))
        yield signal
 
        # Stepping of rotors
        self.stepping.step()
        print('Signal after stepping:   {:2d}  {}  {}'.format(
            signal,
            self.machine.alphabet[signal],
            self.machine.numberline[signal]
            ))
        yield signal
 
        # Pass signal through plugboard
        signal = self.plugboard.forward(signal)
        print('Signal after plugboard:  {:2d}  {}  {}'.format(
            signal,
            self.machine.alphabet[signal],
            self.machine.numberline[signal]
            ))
        yield signal
 
        # Pass signal through rotors from right to left
        for i in range(len(self.rotors)):
            print('+++++ Rotor {} +++++'.format((-i-1)%len(self.rotors) + 1))
            # Generate the iterator for sending the signal through the rotor
            roterator = self.rotors[-i-1].right_to_left(signal)
            signal = next(roterator)   # Enter
            yield signal
            signal = next(roterator)   # Pin
            yield signal
            signal = next(roterator)   # Flat
            yield signal
            signal = next(roterator)   # Exit
            yield signal
            print('Signal after rotor {}:    {:2d}  {}  {}'.format(
                (-i-1)%len(self.rotors) + 1,
                signal,
                self.machine.alphabet[signal],
                self.machine.numberline[signal]
                ))

            yield signal

        # Pass signal through reflector
        signal = self.reflector.reflect(signal)
        print('Signal after reflector:  {:2d}  {}  {}'.format(
            signal,
            self.machine.alphabet[signal],
            self.machine.numberline[signal]
            ))
        yield signal

        # Pass signal through rotors from left to right
        for i in range(len(self.rotors)):
            print('+++++ Rotor {} +++++'.format(i+1))
            # Generate the iterator for sending the signal through the rotor
            roterator = self.rotors[i].left_to_right(signal)
            signal = next(roterator)   # Enter
            yield signal
            signal = next(roterator)   # Flat
            yield signal
            signal = next(roterator)   # Pin
            yield signal
            signal = next(roterator)   # Exit
            yield signal
            print('Signal after rotor {}:    {:2d}  {}  {}'.format(
                i + 1,
                signal,
                self.machine.alphabet[signal],
                self.machine.numberline[signal]
                ))
            yield signal

        # Pass signal through plugboard
        signal = self.plugboard.backward(signal)
        print('Signal after plugboard:  {:2d}  {}  {}'.format(
            signal,
            self.machine.alphabet[signal],
            self.machine.numberline[signal]
            ))
        yield signal

        # Translate processed signal back into letter
        encrypted_letter = self.machine.alphabet[signal]
        self.machine.textcache = self.machine.textcache + encrypted_letter
        print(self.machine.textcache)
        yield encrypted_letter
