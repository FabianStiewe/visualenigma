class Reflector():

    def __init__(self, box, reflector_data):
        self.box = box
        self.length = len(reflector_data[0])
        if self.length != self.box.machine.length:
            raise Exception('Reflector size incompatible with this machine.')
        self.wiring = reflector_data[0]
        print('        Reflector initialized successfully.')

    def reflect(self, enter):
        exit = self.wiring[enter]
        return exit