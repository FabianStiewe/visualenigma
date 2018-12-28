"""This module provides the configuration of the different rotors
and reflectors, i.e. the internal wiring and the notch positions.
It also provides the color scheme for the GUI and some alternative
alphabets."""

ROTOR_I = (

( 4, 10, 12,  5, 11,  6,  3, 16, 21, 25, 13, 19, 14,
 22, 24,  7, 23, 20, 18, 15,  0,  8,  1, 17,  2,  9),

(24,),

'Rotor I'

)


ROTOR_II = (

( 0,  9,  3, 10, 18,  8, 17, 20, 23,  1, 11,  7, 22,
 19, 12,  2, 16,  6, 25, 13, 15, 24,  5, 21, 14,  4),

(12,),

'Rotor II'

)


ROTOR_III = (

( 1,  3,  5,  7,  9, 11,  2, 15, 17, 19, 23, 21, 25,
 13, 24,  4,  8, 22,  6,  0, 10, 12, 20, 18, 16, 14),

(3,),

'Rotor III'

)


ROTOR_IV = (

( 4, 18, 14, 21, 15, 25,  9,  0, 24, 16, 20,  8, 17,
  7, 23, 11, 13,  5, 19,  6, 10,  3,  2, 12, 22,  1),

(17,),

'Rotor IV'

)


ROTOR_V = (

(21, 25,  1, 17,  6,  8, 19, 24, 20, 15, 18,  3, 13,
  7, 11, 23,  0, 22, 12,  9, 16, 14,  5,  4,  2, 10),

(7,),

'Rotor V'

)


ROTOR_VI = (

( 9, 15,  6, 21, 14, 20, 12,  5, 24, 16,  1,  4, 13,
  7, 25, 17,  3, 10,  0, 18, 23, 11,  8,  2, 19, 22),

(7, 20),

'Rotor VI'

)

ROTOR_VII = (

(13, 25,  9,  7,  6, 17,  2, 23, 12, 24, 18, 22,  1,
 14, 20,  5,  0,  8, 21, 11, 15,  4, 10, 16,  3, 19),

(7, 20),

'Rotor VII'

)

ROTOR_VIII = (

( 5, 10, 16,  7, 19, 11, 23, 14,  2,  1,  9, 18, 15,
  3, 25, 17,  0, 12,  4, 22, 13,  8, 20, 24,  6, 21),

(7, 20),

'Rotor VIII'

)

ROTOR_BETA = (

(11,  4, 24,  9, 21,  2, 13,  8, 23, 22, 15,  1, 16,
 12,  3, 17, 19,  0, 10, 25,  6,  5, 20,  7, 14, 18),

(),

'Rotor Beta'

)

ROTOR_GAMMA = (

( 5, 18, 14, 10,  0, 13, 20,  4, 17,  7, 12,  1, 19,
  8, 24,  2, 22, 11, 16, 15, 25, 23, 21,  6,  9,  3),

(),

'Rotor Gamma'

)

UKW_A = (

( 4,  9, 12, 25,  0, 11, 24, 23, 21,  1, 22,  5,  2,
 17, 16, 20, 14, 13, 19, 18, 15,  8, 10,  7,  6,  3),

(),

'UKW A'

)

UKW_B = (

(24, 17, 20,  7, 16, 18, 11,  3, 15, 23, 13,  6, 14,
 10, 12,  8,  4,  1,  5, 25,  2, 22, 21,  9,  0, 19),

(),

'UKW B'

)

UKW_C = (

( 5, 21, 15,  9,  8,  0, 14, 24,  4,  3, 17, 25, 23,
 22,  6,  2, 19, 10, 20, 16, 18,  1, 13, 12,  7, 11),

(),

'UKW C'

)

UKW_B_THIN = (

( 4, 13, 10, 16,  0, 20, 24, 22,  9,  8,  2, 14, 15,
  1, 11, 12,  3, 23, 25, 21,  5, 19,  7, 17,  6, 18),

(),

'UKW B thin'

)

UKW_C_THIN = (

(17,  3, 14,  1,  9, 13, 19, 10, 21,  4,  7, 12, 11,
  5,  2, 22, 25,  0, 23,  6, 24,  8, 15, 18, 20, 16),

(),

'UKW C thin'

)

DEFAULT_ALPHABET = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                    'U', 'V', 'W', 'X', 'Y', 'Z')

DOUBLE_ALPHABET = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                   'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                   'U', 'V', 'W', 'X', 'Y', 'Z',
                   'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                   'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z')

ENIGMA_ALPHABET = ('E','N','I','G','M','A')

SYMBOL_ALPHABET = ('$$', '$&', '$%', '$§', '&$', '&&', '&%', '&§', '%$',
                   '%&', '%%', '%§', '§$', '§&', '§%', '§§', '!!', '!?',
                   '!.', '?!', '??', '?.', '.!', '.?', '..', '==')

DEFAULT_COLOR_SCHEME = {'global_bg': 'white',
                        'plug_key_bg': 'DarkOrange2',
                        'plug_key_fg': 'white',
                        'plug_key_zero_bg': 'DarkOrange2',
                        'plug_key_zero_fg': 'white',
                        'plug_stator_bg': 'DarkOrange2',
                        'plug_stator_fg': 'white',
                        'plug_stator_zero_bg': 'DarkOrange2',
                        'plug_stator_zero_fg': 'white',
                        'plug_c_key_bg': 'gray95',
                        'plug_c_key_fg': 'gray65',
                        'plug_c_key_zero_bg': 'gray95',
                        'plug_c_key_zero_fg': 'gray65',
                        'plug_c_stator_bg': 'gray85',
                        'plug_c_stator_fg': 'white',
                        'plug_c_stator_zero_bg': 'gray85',
                        'plug_c_stator_zero_fg': 'white',
                        'plug_int_top_inactive': 'light grey',
                        'plug_int_top_sunken': 'grey',
                        'plug_int_top_active': 'orange',
                        'plug_int_bottom_inactive': 'white',
                        'plug_int_bottom_active': 'DarkOrange2',
                        'entry_bg': 'DarkGoldenrod4',
                        'entry_fg': 'white',
                        'entry_zero_bg': 'DarkGoldenrod4',
                        'entry_zero_fg': 'white',
                        'pin_bg': 'sienna4',
                        'pin_fg': 'white',
                        'pin_zero_bg': 'sienna4',
                        'pin_zero_fg': 'white',
                        'flat_bg': 'sienna4',
                        'flat_fg': 'white',
                        'flat_zero_bg': 'sienna4',
                        'flat_zero_fg': 'white',
                        'c_pin_bg': 'gray95',
                        'c_pin_fg': 'gray65',
                        'c_pin_zero_bg': 'gray95',
                        'c_pin_zero_fg': 'gray65',
                        'c_flat_bg': 'gray85',
                        'c_flat_fg': 'white',
                        'c_flat_zero_bg': 'gray85',
                        'c_flat_zero_fg': 'white',
                        'ring_bg': 'white',
                        'ring_fg': 'black',
                        'ring_zero_bg': 'red',
                        'ring_zero_fg': 'white',
                        'ring_pos_bg': None,
                        'ring_pos_fg': None,
                        'ring_pos_empty_bg': 'gray75',
                        'ring_pos_empty_fg': None,
                        'ring_pos_zero_bg': None,
                        'ring_pos_zero_fg': None,
                        'ring_pos_current_bg': 'gray85',
                        'ring_pos_current_fg': 'red',
                        'reflector_bg': 'DarkOrange2',
                        'reflector_fg': 'white',
                        'reflector_zero_bg': 'DarkOrange2',
                        'reflector_zero_fg': 'white',
                        'c_reflector_bg': 'gray95',
                        'c_reflector_fg': 'gray65',
                        'c_reflector_zero_bg': 'gray95',
                        'c_reflector_zero_fg': 'gray65',
                        'notch_bg': 'red3',
                        'notch_fg': None,
                        'notch_zero_bg': 'gray75',
                        'notch_zero_fg': None,
                        'notch_empty_bg': 'gray75',
                        'notch_empty_fg': None,
                        'notch_step_bg': 'black',
                        'notch_step_fg': None,
                        'signal_forward_bg': 'green',
                        'signal_forward_fg': None,
                        'signal_backward_bg': 'blue',
                        'signal_backward_fg': None}