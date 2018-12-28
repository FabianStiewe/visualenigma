class SteppingMechanism():

    def __init__(self, box):
        self.box = box
        print('        Stepping mechanism initialized successfully.')

    def step(self):
        if self.box.machine.stepping_mode == 'normal':
            self.normal_step()
        elif self.box.machine.stepping_mode == 'M4':
            self.M4_type_step()
        else:
            raise Exception('Invalid stepping mode!')

    def normal_step(self):
        assert len(self.box.rotors) >= 2
        does_rotate = [False for i in range(len(self.box.rotors))]
        p = self.box.machine.prawl_position

        # Rightmost rotor always moves.
        does_rotate[-1] = True

        # Any rotor in between moves, if either the prawl to its right rests
        # in one of the notches of the rotor to its right, or the prawl to
        # its left rests in one of its own notches. 
        for i in range(1, len(does_rotate)-1):
            does_rotate[i] = (p in self.box.rotors[i+1].notch_positions
                              or p in self.box.rotors[i].notch_positions)

        # Leftmost rotor only moves if the prawl to its right rests in the
        # notch of the rotor to its right.
        does_rotate[0] = p in self.box.rotors[1].notch_positions

        for i in range(len(does_rotate)):
            if does_rotate[i]:
                self.box.rotors[i].rotate()

    def M4_type_step(self):
        assert len(self.box.rotors) >= 3
        does_rotate = [False for i in range(len(self.box.rotors))]
        p = self.box.machine.prawl_position

        # Rightmost rotor always moves.
        does_rotate[-1] = True

        # Any rotor in between moves, if either the prawl to its right rests
        # in one of the notches of the rotor to its right, or the prawl to
        # its left rests in one of its own notches. 
        for i in range(1, len(does_rotate)-1):
            does_rotate[i] = (p in self.box.rotors[i+1].notch_positions
                              or p in self.box.rotors[i].notch_positions)

        # Second rotor from the left only moves if the prawl to its right
        # rests in the notch of the rotor to its right.
        does_rotate[1] = p in self.box.rotors[2].notch_positions

        # Leftmost rotor never moves.
        does_rotate[0] = False

        for i in range(len(does_rotate)):
            if does_rotate[i]:
                self.box.rotors[i].rotate()
         

