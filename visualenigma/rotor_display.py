import tkinter as tk

from visualenigma.stripe import Stripe

class RotorDisplay(tk.Frame):

    def __init__(self, box_int, rotor_number, **kwargs):
        self.box_int = box_int
        super().__init__(master=box_int, bg=self.box_int.gui.color_scheme['global_bg'], **kwargs)
        self.number = rotor_number
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

        dummy = ['' for i in range(self.box_int.gui.machine.length)]

        self.ring = Stripe(self, dummy, relief=tk.RAISED)   

        self.pins = Stripe(self, dummy)

        self.flats = Stripe(self, dummy)

        self.corresponding_pins = Stripe(self, dummy)

        self.corresponding_flats = Stripe(self, dummy)

        self.notches = Stripe(self, dummy)
       
        self.ring_position = Stripe(self, dummy)

    def update(self):

        # ring

        if self.ring_style == 0:
            export = [(i + self.box_int.gui.machine.box.rotors[
                       self.number
                       ].window_letter)
                      % self.box_int.gui.machine.length
                      for i in range(self.box_int.gui.machine.length)]
        elif self.ring_style == 1:
            export = [self.box_int.gui.machine.alphabet[
                      (i + self.box_int.gui.machine.box.rotors[
                       self.number
                       ].window_letter)
                      % self.box_int.gui.machine.length
                      ]
                      for i in range(self.box_int.gui.machine.length)]
        elif self.ring_style == 2:
            export = [self.box_int.gui.machine.numberline[
                      (i + self.box_int.gui.machine.box.rotors[
                       self.number
                       ].window_letter)
                      % self.box_int.gui.machine.length
                      ]
                      for i in range(self.box_int.gui.machine.length)]
        elif self.ring_style == 3:
            export = ['' for i in range(self.box_int.gui.machine.length)]
        self.ring.configure(
          symbols=export,
          fg=self.box_int.gui.color_scheme['ring_fg'],
          bg=self.box_int.gui.color_scheme['ring_bg']
          )
        self.ring.squares[0].configure(
          fg=self.box_int.gui.color_scheme['ring_zero_fg'],
          bg=self.box_int.gui.color_scheme['ring_zero_bg']
          )

        # pins

        if self.pin_style == 0:
            export = [(i - self.box_int.gui.machine.box.rotors[
                       self.number
                       ].zero)
                      % self.box_int.gui.machine.length
                      for i in range(self.box_int.gui.machine.length)]
        elif self.pin_style == 1:
            export = [self.box_int.gui.machine.alphabet[
                      (i - self.box_int.gui.machine.box.rotors[
                       self.number
                       ].zero)
                      % self.box_int.gui.machine.length
                      ]
                      for i in range(self.box_int.gui.machine.length)]
        elif self.pin_style == 2:
            export = [self.box_int.gui.machine.numberline[
                      (i - self.box_int.gui.machine.box.rotors[
                       self.number
                       ].zero)
                      % self.box_int.gui.machine.length
                      ]
                      for i in range(self.box_int.gui.machine.length)]
        elif self.pin_style == 3:
            export = ['' for i in range(self.box_int.gui.machine.length)]
        self.pins.configure(
          symbols=export,
          fg=self.box_int.gui.color_scheme['pin_fg'],
          bg=self.box_int.gui.color_scheme['pin_bg']
          )
        self.pins.squares[0].configure(
          fg=self.box_int.gui.color_scheme['pin_zero_fg'],
          bg=self.box_int.gui.color_scheme['pin_zero_bg']
          )

        # flats

        if self.flat_style == 0:
            export = [(i - self.box_int.gui.machine.box.rotors[
                       self.number
                       ].zero)
                      % self.box_int.gui.machine.length
                      for i in range(self.box_int.gui.machine.length)]
        elif self.flat_style == 1:
            export = [self.box_int.gui.machine.alphabet[
                      (i - self.box_int.gui.machine.box.rotors[
                       self.number
                       ].zero)
                      % self.box_int.gui.machine.length
                      ]
                      for i in range(self.box_int.gui.machine.length)]
        elif self.flat_style == 2:
            export = [self.box_int.gui.machine.numberline[
                      (i - self.box_int.gui.machine.box.rotors[
                       self.number
                       ].zero)
                      % self.box_int.gui.machine.length
                      ]
                      for i in range(self.box_int.gui.machine.length)]
        elif self.flat_style == 3:
            export = ['' for i in range(self.box_int.gui.machine.length)]
        self.flats.configure(
          symbols=export,
          fg=self.box_int.gui.color_scheme['flat_fg'],
          bg=self.box_int.gui.color_scheme['flat_bg']
          )
        self.flats.squares[0].configure(
          fg=self.box_int.gui.color_scheme['flat_zero_fg'],
          bg=self.box_int.gui.color_scheme['flat_zero_bg']
          )

        # corresponding pins

        if self.cor_pin_style == 0:
            export = [self.box_int.gui.machine.box.rotors[self.number].pins[
                      (i - self.box_int.gui.machine.box.rotors[
                       self.number
                       ].zero)
                      % self.box_int.gui.machine.length
                      ]
                      for i in range(self.box_int.gui.machine.length)]
        elif self.cor_pin_style == 1:
            export = [self.box_int.gui.machine.alphabet[
                      self.box_int.gui.machine.box.rotors[self.number].pins[
                      (i - self.box_int.gui.machine.box.rotors[
                       self.number
                       ].zero)
                      % self.box_int.gui.machine.length
                      ]]
                      for i in range(self.box_int.gui.machine.length)]
        elif self.cor_pin_style == 2:
            export = [self.box_int.gui.machine.numberline[
                      self.box_int.gui.machine.box.rotors[self.number].pins[
                      (i - self.box_int.gui.machine.box.rotors[
                       self.number
                       ].zero)
                      % self.box_int.gui.machine.length
                      ]]
                      for i in range(self.box_int.gui.machine.length)]
        elif self.cor_pin_style == 3:
            export = ['' for i in range(self.box_int.gui.machine.length)]
        self.corresponding_pins.configure(
            symbols=export,
            fg=self.box_int.gui.color_scheme['c_pin_fg'],
            bg=self.box_int.gui.color_scheme['c_pin_bg']
            )
        self.corresponding_pins.squares[0].configure(
            fg=self.box_int.gui.color_scheme['c_pin_zero_fg'],
            bg=self.box_int.gui.color_scheme['c_pin_zero_bg']
            )

        # corresponding flats

        if self.cor_flat_style == 0:
            export = [self.box_int.gui.machine.box.rotors[self.number].flats[
                      (i - self.box_int.gui.machine.box.rotors[
                       self.number
                       ].zero)
                      % self.box_int.gui.machine.length
                      ]
                      for i in range(self.box_int.gui.machine.length)]
        elif self.cor_flat_style == 1:
            export = [self.box_int.gui.machine.alphabet[
                      self.box_int.gui.machine.box.rotors[self.number].flats[
                      (i - self.box_int.gui.machine.box.rotors[
                       self.number
                       ].zero)
                      % self.box_int.gui.machine.length
                      ]]
                      for i in range(self.box_int.gui.machine.length)]
        elif self.cor_flat_style == 2:
            export = [self.box_int.gui.machine.numberline[
                      self.box_int.gui.machine.box.rotors[
                      self.number
                      ].flats[
                      (i - self.box_int.gui.machine.box.rotors[
                       self.number
                       ].zero)
                      % self.box_int.gui.machine.length
                      ]]
                      for i in range(self.box_int.gui.machine.length)]
        elif self.cor_flat_style == 3:
            export = ['' for i in range(self.box_int.gui.machine.length)]
        self.corresponding_flats.configure(
            symbols=export,
            fg=self.box_int.gui.color_scheme['c_flat_fg'],
            bg=self.box_int.gui.color_scheme['c_flat_bg']
            )
        self.corresponding_flats.squares[0].configure(
            fg=self.box_int.gui.color_scheme['c_flat_zero_fg'],
            bg=self.box_int.gui.color_scheme['c_flat_zero_bg']
            )

        # notches

        dummy = ['' for i in range(self.box_int.gui.machine.length)]

        self.notches.configure(    
            symbols=dummy,
            fg=self.box_int.gui.color_scheme['notch_empty_fg'],
            bg=self.box_int.gui.color_scheme['notch_empty_bg']
            )
        self.notches.squares[0].configure(
            bg=self.box_int.gui.color_scheme['notch_zero_bg']
            )
        if self.number > 1 or (self.box_int.gui.machine.stepping_mode == 'normal' and self.number > 0):
            self.notches.squares[self.box_int.gui.machine.prawl_position].configure(
                bg=self.box_int.gui.color_scheme['notch_step_bg']
                )
        for n in self.box_int.gui.machine.box.rotors[
                    self.number
                    ].notch_positions:
            self.notches.squares[n].configure(
                bg=self.box_int.gui.color_scheme['notch_bg']
                )

        # ring position

        self.ring_position.configure(
            symbols=dummy,
            fg=self.box_int.gui.color_scheme['ring_pos_empty_fg'],
            bg=self.box_int.gui.color_scheme['ring_pos_empty_bg']
            )

        export = ['' for i in range(self.box_int.gui.machine.length)]
        export[self.box_int.gui.machine.box.rotors[self.number].zero] = '\u25c0'
        self.ring_position.configure(symbols=export)
        self.ring_position.squares[0].configure(
            fg=self.box_int.gui.color_scheme['ring_pos_zero_fg'],
            bg=self.box_int.gui.color_scheme['ring_pos_zero_bg']
            )
        self.ring_position.squares[
            self.box_int.gui.machine.box.rotors[self.number].zero
            ].configure(fg=self.box_int.gui.color_scheme['ring_pos_current_fg'],
                        bg=self.box_int.gui.color_scheme['ring_pos_current_bg'])
