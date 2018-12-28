import tkinter as tk

from visualenigma.machine_data import DEFAULT_ALPHABET, DEFAULT_COLOR_SCHEME

class Key(tk.Canvas):

    def __init__(self, master, text):
        super().__init__(master, width=50, height=50,
                         bg=DEFAULT_COLOR_SCHEME['global_bg'],
                         bd=0, highlightthickness=0, relief='raised')
        self.command = lambda: print('Key response not defined.')
        pad = 8
        ow = 4
        x0 = pad + ow / 2
        x1 = 50 - x0
        y0 = pad + ow / 2
        y1 = 50 - y0
        self.create_oval(x0, y0, x1, y1,
                         fill='black', outline='grey', width=ow,
                         tags=('circle',))
        self.create_text((x0 + x1) / 2, (y0 + y1) / 2,
                         fill='white',
                         text=text,
                         tags=('letter',))
        self.bind('<Enter>', self.on_enter)
        self.bind('<Leave>', self.on_leave)
        self.bind('<ButtonPress-1>', self.on_press)
        self.bind('<ButtonRelease-1>', self.on_release)

    def on_enter(self, event):
        self.itemconfig('circle', fill='grey', outline='white')

    def on_leave(self, event):
        self.itemconfig('circle', fill='black', outline='grey')

    def on_press(self, event):
        self.itemconfig('circle', fill='white', outline='black')
        self.itemconfig('letter', fill='black')
        self.config(relief='sunken')
        self.command()

    def on_release(self, event):
        self.itemconfig('circle', fill='black', outline='grey')
        self.itemconfig('letter', fill='white')
        self.config(relief='raised')
        

class KeyboardInterface(tk.Frame):

    def __init__(self, gui):
        super().__init__(master=gui, padx=20,
                         bg=DEFAULT_COLOR_SCHEME['global_bg'])
        self.gui = gui
        if self.gui.machine.alphabet == DEFAULT_ALPHABET:
            letter_order = ('Q', 'W', 'E', 'R', 'T', 'Z', 'U', 'I', 'O',
                            'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K',
                            'P', 'Y', 'X', 'C', 'V', 'B', 'N', 'M', 'L')
        else:
            letter_order = self.gui.machine.alphabet

        # Help function
        def send(x):
            def f():
                self.gui.visualize(x)
            return f

        # Create keys
        self.keys = []
        for i in range(len(letter_order)):
            letter = letter_order[i]
            self.keys.append(Key(master=self, text=letter))
            self.keys[i].command = send(letter)

        # Place keys in rows alternating between 9 and 8 keys per row
        complete_blocks = len(letter_order) // 17
        for n in range(complete_blocks):
            for i in range(9):        
                self.keys[17*n+i].grid(row=2*n, column=2*i, columnspan=2)
            for i in range(8):        
                self.keys[17*n+i+9].grid(row=2*n+1, column=2*i+1,
                                         columnspan=2)
        if len(letter_order) % 17 <= 9:
            for i in range(len(letter_order) % 17):        
                self.keys[17*complete_blocks+i].grid(
                    row=2*complete_blocks,
                    column=2*i,
                    columnspan=2
                    )
        else:
            for i in range(9):        
                self.keys[17*complete_blocks+i].grid(
                    row=2*complete_blocks,
                    column=2*i,
                    columnspan=2
                    )
            for i in range(len(letter_order) % 17 - 9):        
                self.keys[17*complete_blocks+9+i].grid(
                    row=2*complete_blocks+1,
                    column=2*i+1,
                    columnspan=2
                    )
        print('        Keyboard interface initialized successfully.')
