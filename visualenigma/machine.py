from numpy import arange
from random import shuffle, sample

from visualenigma.box import Box
from visualenigma.gui import GUI
import visualenigma.machine_data as md

class CipheringMachine():

    """The rotor machine itself.

    When instantiated, it automatically builds all its components
    (rotors, reflector, plugboard) and the GUI."""

    def __init__(self, master,
                 alphabet=md.DEFAULT_ALPHABET,
                 rotor_set=[md.ROTOR_I, md.ROTOR_II, md.ROTOR_III],
                 reflector=md.UKW_B,
                 prawl_position=8,
                 stepping_mode='normal'):
        print('Initializing ciphering machine...')
        self.alphabet = alphabet
        self.rotor_set = rotor_set
        self.reflector = reflector
        self.prawl_position = prawl_position
        self.stepping_mode = stepping_mode
        self.length = len(self.alphabet)
        if self.prawl_position >= self.length:
            raise Exception('Prawl position greater than alphabet length.')
        self.indices = self.letterpositions(self.alphabet)
        self.numberline = ['{:02d}'.format(i + 1)
                           for i in range(self.length)]
        self.textcache = ''
        print('    Initializing box...')
        self.box = Box(self)
        print('    Initializing GUI...')
        self.gui = GUI(self, master)
        print('Ciphering machine initialized successfully.')


    @staticmethod
    def letterpositions(alphabet):
        numbers = {alphabet[i]: i for i in range(len(alphabet))}
        return numbers

    @staticmethod
    def create_random_rotor(length, number_of_notches, name='Random'):
        if number_of_notches > length:
            raise Exception('Failed to create random rotor: '
                            'number of notches must not exceed rotor size!')
        wiring = arange(length)
        shuffle(wiring)
        wiring = tuple(wiring)
        notches = tuple(sorted(sample(wiring, number_of_notches)))
        rotor = (wiring, notches, name)
        return rotor
