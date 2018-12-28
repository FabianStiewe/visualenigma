class Plugboard():

    def __init__(self, box):
        self.box = box
        self.wiring = {k: k for k in range(self.box.machine.length)}
        self.status = [(self.box.machine.alphabet[k],
                        self.box.machine.alphabet[v])
                       for k, v in self.wiring.items()]

        print('        Plugboard initialized successfully.')

    def swap(self, a, b):
        if (self.wiring[a] == a and self.wiring[b] == b):
            self.wiring[a] = b
            self.wiring[b] = a
        elif (self.wiring[a] == b and self.wiring[b] == a):
            self.wiring[a] = a
            self.wiring[b] = b
        else:
            print('At least one contact already plugged elsewhere.')
        self.status = [(self.box.machine.alphabet[k],
                        self.box.machine.alphabet[v])
                       for k, v in self.wiring.items()]

    def forward(self, enter):
        exit = self.wiring[enter]
        return exit

    def backward(self, enter):
        exit = self.wiring[enter]
        return exit
