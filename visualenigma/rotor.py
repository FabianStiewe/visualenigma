class Rotor():

    def __init__(self, box, rotor_data,
                 ring_position=0, window_letter=0):
        self.box = box

        self.length = len(rotor_data[0])
        if self.length != self.box.machine.length:
            raise Exception('Rotor size incompatible with this machine.')

        self.flats = dict(zip(range(self.length), rotor_data[0]))
        self.pins = {v: k for k, v in self.flats.items()}

        self.notches = rotor_data[1]
        for n in self.notches:
            if n >= self.length:
                raise Exception('Notch position on rotor invalid.')

        self.ring_position = ring_position

        self.window_letter = window_letter

        self.zero = (self.ring_position - self.window_letter) % self.length

        self.notch_positions = [(n - self.window_letter) % self.length
                                for n in self.notches]

        print('        Rotor initialized successfully.')
        
    def rotate(self, steps=1):
        self.window_letter = (self.window_letter + steps) % self.length
        self.zero = (self.ring_position - self.window_letter) % self.length
        self.notch_positions = [(n - self.window_letter) % self.length
                                for n in self.notches]

    def adjust_ring(self, steps=1):
        self.ring_position = (self.ring_position + steps) % self.length
        self.window_letter = (self.window_letter + steps) % self.length
        self.notch_positions = [(n - self.window_letter) % self.length
                                for n in self.notches]

    def adjust_zero(self, steps=1):
        self.zero = (self.zero + steps) % self.length
        self.ring_position = (self.ring_position + steps) % self.length

    def right_to_left(self, enter):

        print('Enter:                   {:2d}  {}  {}'.format(
            enter,
            self.box.machine.alphabet[enter],
            self.box.machine.numberline[enter]
            ))

        yield enter

        pin = (enter - self.zero) % self.length

        print('Pin:                     {:2d}  {}  {}'.format(
            pin,
            self.box.machine.alphabet[pin],
            self.box.machine.numberline[pin]
            ))

        yield pin

        flat = self.flats[pin]

        print('Flat:                    {:2d}  {}  {}'.format(
            flat,
            self.box.machine.alphabet[flat],
            self.box.machine.numberline[flat]
            ))

        yield flat

        exit = (flat + self.zero) % self.length

        print('Exit:                    {:2d}  {}  {}'.format(
            exit,
            self.box.machine.alphabet[exit],
            self.box.machine.numberline[exit]
            ))        

        yield exit

    def left_to_right(self, enter):

        print('Enter:                   {:2d}  {}  {}'.format(
            enter,
            self.box.machine.alphabet[enter],
            self.box.machine.numberline[enter]
            ))

        yield enter

        flat = (enter - self.zero) % self.length

        print('Flat:                    {:2d}  {}  {}'.format(
            flat,
            self.box.machine.alphabet[flat],
            self.box.machine.numberline[flat]
            ))

        yield flat

        pin = self.pins[flat]

        print('Pin:                     {:2d}  {}  {}'.format(
            pin,
            self.box.machine.alphabet[pin],
            self.box.machine.numberline[pin]
            ))

        yield pin

        exit = (pin + self.zero) % self.length

        print('Exit:                    {:2d}  {}  {}'.format(
            exit,
            self.box.machine.alphabet[exit],
            self.box.machine.numberline[exit]
            )) 

        yield exit
