from numpy import arange
from random import shuffle, sample

def letterpositions(alphabet):
    numbers = {alphabet[i]: i for i in range(len(alphabet))}
    return numbers


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

# rotor_display utils

def empty_string_list(length):
    return ['' for i in range(length)]

def update_component(machine,
                     color_scheme,
                     component,
                     style,
                     component_string,
                     rotor_number,
                     func):

    rotors = machine.box.rotors
    length = machine.length
    alphabet = machine.alphabet
    numberline = machine.numberline
    scheme = color_scheme
    n = rotor_number

    f = lambda i: func(i, rotors, n, length)

    if style == 0:
        export = [f(i) for i in range(length)]
    elif style == 1:
        export = [alphabet[f(i)] for i in range(length)]
    elif style == 2:
        export = [numberline[f(i)] for i in range(length)]
    elif style == 3:
        export = ['' for i in range(length)]
      
    component.configure(
        symbols=export,
        fg=scheme[component_string + '_fg'],
        bg=scheme[component_string + '_bg']
        )
    component.squares[0].configure(
        fg=scheme[component_string + '_zero_fg'],
        bg=scheme[component_string + '_zero_bg']
        )

def update_notches(machine,
                   color_scheme,
                   notches,
                   dummy,
                   rotor_number):

    rotors = machine.box.rotors
    scheme = color_scheme
    n = rotor_number

    notches.configure(    
        symbols=dummy,
        fg=scheme['notch_empty_fg'],
        bg=scheme['notch_empty_bg']
        )
    notches.squares[0].configure(
        bg=scheme['notch_zero_bg']
        )
    if n > 1 or (machine.stepping_mode == 'normal' and n > 0):
        notches.squares[machine.prawl_position].configure(
            bg=scheme['notch_step_bg']
            )
    for k in rotors[n].notch_positions:
        notches.squares[k].configure(
            bg=scheme['notch_bg']
            )

def update_ring_position(machine,
                         color_scheme,
                         ring_position,
                         dummy,
                         rotor_number):

    rotors = machine.box.rotors
    scheme = color_scheme
    n = rotor_number
    length = machine.length

    ring_position.configure(
        symbols=dummy,
        fg=scheme['ring_pos_empty_fg'],
        bg=scheme['ring_pos_empty_bg']
        )

    export = list(dummy)
    export[rotors[n].zero] = '\u25c0'
    ring_position.configure(symbols=export)
    ring_position.squares[0].configure(
        fg=scheme['ring_pos_zero_fg'],
        bg=scheme['ring_pos_zero_bg']
        )
    ring_position.squares[
        rotors[n].zero
        ].configure(fg=scheme['ring_pos_current_fg'],
                    bg=scheme['ring_pos_current_bg'])