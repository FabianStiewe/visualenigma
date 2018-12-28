import tkinter as tk

import visualenigma.machine_data as md
from visualenigma.rotor import Rotor
from visualenigma.reflector import Reflector
from visualenigma.machine_data import DEFAULT_COLOR_SCHEME

class ControlsInterface(tk.Frame):

    """Buttons and dropdown menus for machine and GUI configuration."""

    def __init__(self, gui):
        super().__init__(master=gui,
                         bg=DEFAULT_COLOR_SCHEME['global_bg'])
        self.gui = gui
        self.rotor_movement_controls()
        self.display_style_controls()
        self.rotor_and_reflector_selection_controls()
        self.stepping_mode_control()
        self.lid_control()
        print('        Controls interface initialized successfully.')

    def rotor_movement_controls(self):
        """Create buttons for moving the rotors."""

        # Help function
        def move(name, i):
            """Return a function to move either a whole rotor, a rotor's ring
            or a rotor's contacts one step up or down."""
            if name == 'r_up':
                def f():
                    self.gui.machine.box.rotors[i].adjust_ring(1)
                    self.gui.box_int.update_rotors()
            elif name == 'r_down':
                def f():
                    self.gui.machine.box.rotors[i].adjust_ring(-1)
                    self.gui.box_int.update_rotors()
            elif name == 'l_up':
                def f():
                    self.gui.machine.box.rotors[i].rotate(1)
                    self.gui.box_int.update_rotors()
            elif name == 'l_down':
                def f():
                    self.gui.machine.box.rotors[i].rotate(-1)
                    self.gui.box_int.update_rotors()
            elif name == 'z_up':
                def f():
                    self.gui.machine.box.rotors[i].adjust_zero(1)
                    self.gui.box_int.update_rotors()
            elif name == 'z_down':
                def f():
                    self.gui.machine.box.rotors[i].adjust_zero(-1)
                    self.gui.box_int.update_rotors()
            return f

        # Create buttons
        self.move_label = tk.Label(self, text='Move rotors:',
                                   bg=DEFAULT_COLOR_SCHEME['global_bg'])
        self.move_label.grid(row=2, column=0, columnspan=3, sticky=tk.W)
        self.ring_up = []
        self.letter_up = []
        self.zero_up = []
        self.ring_down = []
        self.letter_down = []
        self.zero_down = []
        for i in range(len(self.gui.machine.box.rotors)):
            self.ring_up.append(tk.Button(
                self, width=5,
                text=str(i+1)+'\u2193_',
                command=move('r_up', i),
                highlightbackground=DEFAULT_COLOR_SCHEME['global_bg']
                ))
            self.ring_up[i].grid(row=4, column=3*i)
            self.ring_down.append(tk.Button(
                self, width=5,
                text=str(i+1)+'\u2191_',
                command=move('r_down', i),
                highlightbackground=DEFAULT_COLOR_SCHEME['global_bg']
                ))
            self.ring_down[i].grid(row=3, column=3*i)
            self.letter_up.append(tk.Button(
                self, width=5,
                text=str(i+1)+'\u2193\u2193',
                command=move('l_up', i),
                highlightbackground=DEFAULT_COLOR_SCHEME['global_bg']
                ))
            self.letter_up[i].grid(row=4, column=3*i+1)
            self.letter_down.append(tk.Button(
                self, width=5,
                text=str(i+1)+'\u2191\u2191',
                command=move('l_down', i),
                highlightbackground=DEFAULT_COLOR_SCHEME['global_bg']
                ))
            self.letter_down[i].grid(row=3, column=3*i+1)
            self.zero_up.append(tk.Button(
                self, width=5,
                text=str(i+1)+'_\u2191',
                command=move('z_up', i),
                highlightbackground=DEFAULT_COLOR_SCHEME['global_bg']
                ))
            self.zero_up[i].grid(row=3, column=3*i+2)
            self.zero_down.append(tk.Button(
                self, width=5,
                text=str(i+1)+'_\u2193',
                command=move('z_down', i),
                highlightbackground=DEFAULT_COLOR_SCHEME['global_bg']
                ))
            self.zero_down[i].grid(row=4, column=3*i+2)

    def display_style_controls(self):
        """Create buttons to change the display style of the components."""
        
        # Help function
        def change_style(name):
            """Return a function to cycle through the display styles of a
            box interface's component: numbers starting at 0, letters,
            numbers starting at 01, or empty."""
            if name == 'ring_style':
                def f():
                    for i in range(len(self.gui.machine.box.rotors)):
                        self.gui.box_int.rotors_disp[i].ring_style += 1
                        self.gui.box_int.rotors_disp[i].ring_style %= 4
                        self.gui.box_int.update_all()
            elif name == 'pin_style':
                def f():
                    for i in range(len(self.gui.machine.box.rotors)):
                        self.gui.box_int.rotors_disp[i].pin_style += 1
                        self.gui.box_int.rotors_disp[i].pin_style %= 4
                        self.gui.box_int.update_all()
            elif name == 'c_pin_style':
                def f():
                    for i in range(len(self.gui.machine.box.rotors)):
                        self.gui.box_int.rotors_disp[i].cor_pin_style += 1
                        self.gui.box_int.rotors_disp[i].cor_pin_style %= 4
                        self.gui.box_int.update_all()
            elif name == 'flat_style':
                def f():
                    for i in range(len(self.gui.machine.box.rotors)):
                        self.gui.box_int.rotors_disp[i].flat_style += 1
                        self.gui.box_int.rotors_disp[i].flat_style %= 4
                        self.gui.box_int.update_all()
            elif name == 'c_flat_style':
                def f():
                    for i in range(len(self.gui.machine.box.rotors)):
                        self.gui.box_int.rotors_disp[i].cor_flat_style += 1
                        self.gui.box_int.rotors_disp[i].cor_flat_style %= 4
                        self.gui.box_int.update_all()
            elif name == 'entry_style':
                def f():
                    self.gui.box_int.entry_stator_disp.contacts_style += 1
                    self.gui.box_int.entry_stator_disp.contacts_style %= 4
                    self.gui.box_int.update_all()
            elif name == 'reflector_style':
                def f():
                    self.gui.box_int.reflector_disp.contacts_style += 1
                    self.gui.box_int.reflector_disp.contacts_style %= 4
                    self.gui.box_int.update_all()
            elif name == 'c_reflector_style':
                def f():
                    self.gui.box_int.reflector_disp.cor_contacts_style += 1
                    self.gui.box_int.reflector_disp.cor_contacts_style %= 4
                    self.gui.box_int.update_all()
            elif name == 'plug_key_style':
                def f():
                    self.gui.box_int.plugboard_disp.kb_contacts_style += 1
                    self.gui.box_int.plugboard_disp.kb_contacts_style %= 4
                    self.gui.box_int.update_all()
            elif name == 'plug_stator_style':
                def f():
                    self.gui.box_int.plugboard_disp.cor_es_contacts_style += 1
                    self.gui.box_int.plugboard_disp.cor_es_contacts_style %= 4
                    self.gui.box_int.update_all()
            elif name == 'plug_c_key_style':
                def f():
                    self.gui.box_int.plugboard_disp.cor_kb_contacts_style += 1
                    self.gui.box_int.plugboard_disp.cor_kb_contacts_style %= 4
                    self.gui.box_int.update_all()
            elif name == 'plug_c_stator_style':
                def f():
                    self.gui.box_int.plugboard_disp.es_contacts_style += 1
                    self.gui.box_int.plugboard_disp.es_contacts_style %= 4
                    self.gui.box_int.update_all()
            return f

        # Create buttons
        self.style_label = tk.Label(self, text='Change display style:',
                                    bg=DEFAULT_COLOR_SCHEME[
                                    'global_bg'
                                    ])
        self.style_label.grid(row=7, column=0, columnspan=3, sticky=tk.W)
        self.ring_style = tk.Button(
            self, width=5,
            text='R',
            command=change_style('ring_style'),
            highlightbackground=DEFAULT_COLOR_SCHEME['global_bg']
            )
        self.ring_style.grid(row=8, column=0)
        self.pin_style = tk.Button(
            self, width=5,
            text='P',
            command=change_style('pin_style'),
            highlightbackground=DEFAULT_COLOR_SCHEME['global_bg']
            )
        self.pin_style.grid(row=8, column=1)
        self.c_pin_style = tk.Button(
            self, width=5,
            text='CP',
            command=change_style('c_pin_style'),
            highlightbackground=DEFAULT_COLOR_SCHEME['global_bg']
            )
        self.c_pin_style.grid(row=8, column=2)
        self.flat_style = tk.Button(
            self, width=5,
            text='F',
            command=change_style('flat_style'),
            highlightbackground=DEFAULT_COLOR_SCHEME['global_bg']
            )
        self.flat_style.grid(row=8, column=3)
        self.c_flat_style = tk.Button(
            self, width=5,
            text='CF',
            command=change_style('c_flat_style'),
            highlightbackground=DEFAULT_COLOR_SCHEME['global_bg']
            )
        self.c_flat_style.grid(row=8, column=4)
        self.entry_style = tk.Button(
            self, width=5,
            text='ES',
            command=change_style('entry_style'),
            highlightbackground=DEFAULT_COLOR_SCHEME['global_bg']
            )
        self.entry_style.grid(row=8, column=5)
        self.reflector_style = tk.Button(
            self, width=5,
            text='RF',
            command=change_style('reflector_style'),
            highlightbackground=DEFAULT_COLOR_SCHEME['global_bg']
            )
        self.reflector_style.grid(row=9, column=0)
        self.c_reflector_style = tk.Button(
            self, width=5,
            text='CRF',
            command=change_style('c_reflector_style'),
            highlightbackground=DEFAULT_COLOR_SCHEME['global_bg']
            )
        self.c_reflector_style.grid(row=9, column=1)
        self.plug_key_style = tk.Button(
            self, width=5,
            text='PK', command=change_style('plug_key_style'),
            highlightbackground=DEFAULT_COLOR_SCHEME['global_bg']
            )
        self.plug_key_style.grid(row=9, column=2)
        self.plug_stator_style = tk.Button(
            self, width=5,
            text='PS',
            command=change_style('plug_stator_style'),
            highlightbackground=DEFAULT_COLOR_SCHEME['global_bg']
            )
        self.plug_stator_style.grid(row=9, column=3)
        self.plug_c_key_style = tk.Button(
            self, width=5,
            text='CPK', command=change_style('plug_c_key_style'),
            highlightbackground=DEFAULT_COLOR_SCHEME['global_bg']
            )
        self.plug_c_key_style.grid(row=9, column=4)
        self.plug_c_stator_style = tk.Button(
            self, width=5,
            text='CPS',
            command=change_style('plug_c_stator_style'),
            highlightbackground=DEFAULT_COLOR_SCHEME['global_bg']
            )
        self.plug_c_stator_style.grid(row=9, column=5)

    def rotor_and_reflector_selection_controls(self):
        """Create dropdown menus for selecting rotors and reflector."""

        available = (md.ROTOR_I,
                     md.ROTOR_II,
                     md.ROTOR_III,
                     md.ROTOR_IV,
                     md.ROTOR_V,
                     md.ROTOR_VI,
                     md.ROTOR_VII,
                     md.ROTOR_VIII,
                     md.ROTOR_BETA,
                     md.ROTOR_GAMMA,
                     md.UKW_A,
                     md.UKW_B,
                     md.UKW_C,
                     md.UKW_B_THIN,
                     md.UKW_C_THIN)
        equipment = {r[2]: r for r in available}
        self.select_rotor = []
        self.rotor_vars = []

        # Help function for selecting rotors
        def change_rotor(i):
            """Return a function to place a new rotor at position i."""
            def f(*args):
                rp = self.gui.machine.box.rotors[i].ring_position
                wl = self.gui.machine.box.rotors[i].window_letter
                self.gui.machine.rotor_set[i] = equipment[
                                                    self.rotor_vars[i].get()
                                                    ]
                self.gui.machine.box.rotors[i] = Rotor(
                    self.gui.machine.box,
                    self.gui.machine.rotor_set[i],
                    rp, wl
                    )
                self.gui.box_int.update_all()
            return f

        # Create dropdown menus for selecting rotors
        self.rotor_label = tk.Label(self, text='Select rotors:',
                                    bg=DEFAULT_COLOR_SCHEME['global_bg'])
        self.rotor_label.grid(row=0, column=0, columnspan=3, sticky=tk.W)
        for i in range(len(self.gui.machine.box.rotors)):
            self.rotor_vars.append(tk.StringVar())
            self.rotor_vars[i].set(self.gui.machine.rotor_set[i][2])
            self.select_rotor.append(tk.OptionMenu(
                self,
                self.rotor_vars[i],
                *equipment.keys()
                ))
            self.select_rotor[i].configure(bg=DEFAULT_COLOR_SCHEME[
                                                'global_bg'
                                                ])
            self.select_rotor[i].grid(row=1, column=i*3, columnspan=3,
                                      sticky=tk.W+tk.E)
            self.rotor_vars[i].trace('w', callback=change_rotor(i))

        # Help function for selecting reflector
        def change_reflector(*args):
            self.gui.machine.reflector = equipment[self.reflector_var.get()]
            self.gui.machine.box.reflector = Reflector(
                self.gui.machine.box,
                self.gui.machine.reflector
                )
            self.gui.box_int.update_all()

        # Create dropdown menu for selecting reflector
        self.reflector_label = tk.Label(self, text='Select reflector:',
                                        bg=DEFAULT_COLOR_SCHEME['global_bg'])
        self.reflector_label.grid(row=5, column=0, columnspan=3, sticky=tk.W)
        self.reflector_var = tk.StringVar()
        self.reflector_var.set(self.gui.machine.reflector[2])
        self.select_reflector = tk.OptionMenu(
            self,
            self.reflector_var,
            *equipment.keys()
            )
        self.select_reflector.configure(bg=DEFAULT_COLOR_SCHEME['global_bg'])
        self.select_reflector.grid(row=6, column=0, columnspan=3,
                                   sticky=tk.W+tk.E)
        self.reflector_var.trace('w', callback=change_reflector)



    def stepping_mode_control(self):
        """Create radiobuttons for switching stepping mode between
        'normal' and 'M4'"""

        # Help function 
        def switch_stepping_mode(*args):
            self.gui.machine.stepping_mode = self.stepping_var.get()
            self.gui.box_int.update_all()
        
        # Create radiobuttons
        self.stepping_label = tk.Label(self, text='Stepping mode:',
                                       bg=DEFAULT_COLOR_SCHEME['global_bg'])
        self.stepping_label.grid(row=5, column=3, columnspan=3)
        self.stepping_var = tk.StringVar()
        self.stepping_var.set(self.gui.machine.stepping_mode)
        self.switch_mode = [tk.Radiobutton(self, text='Normal',
                                           variable=self.stepping_var,
                                           value='normal',
                                           bg=DEFAULT_COLOR_SCHEME[
                                               'global_bg'
                                               ]),
                            tk.Radiobutton(self, text='M4',
                                           variable=self.stepping_var,
                                           value='M4',
                                           bg=DEFAULT_COLOR_SCHEME[
                                               'global_bg'
                                               ])]
        self.switch_mode[0].grid(row=5, column=6, columnspan=3, sticky=tk.W)
        self.switch_mode[1].grid(row=6, column=6, columnspan=3, sticky=tk.W)
        self.stepping_var.trace('w', callback=switch_stepping_mode)



    def lid_control(self):
        """Create checkbox for opening and closing the lid, i.e. revealing
        or hiding the internal signal processing"""

        # Help function
        def open_or_close(*args):
            closed_lid = {k: 'brown' for k in DEFAULT_COLOR_SCHEME.keys()}
            closed_lid.update({'ring_zero_bg': 'red',
                           'ring_zero_fg': 'white'})
            if self.lid_var.get():
                self.gui.color_scheme = DEFAULT_COLOR_SCHEME
            else:
                self.gui.color_scheme = closed_lid
            self.gui.box_int.configure(bg=self.gui.color_scheme['global_bg'])
            self.gui.box_int.plugboard_disp.configure(
                bg=self.gui.color_scheme['global_bg']
                )
            self.gui.box_int.entry_stator_disp.configure(
                bg=self.gui.color_scheme['global_bg']
                )
            self.gui.box_int.reflector_disp.configure(
                bg=self.gui.color_scheme['global_bg']
                )
            for rotor in self.gui.box_int.rotors_disp:
                rotor.configure(bg=self.gui.color_scheme['global_bg'])
            self.gui.box_int.update_all()

        # Create checkbutton
        self.lid_var = tk.IntVar()
        self.lid_var.set(1)
        self.lid_checkbutton = tk.Checkbutton(self, text='Lid open',
                                              variable=self.lid_var,
                                              command=open_or_close,
                                              bg=DEFAULT_COLOR_SCHEME[
                                                  'global_bg'
                                                  ])
        self.lid_checkbutton.grid(row=5, column=9, columnspan=3, sticky=tk.W)


        