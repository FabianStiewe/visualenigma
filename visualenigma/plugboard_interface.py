import tkinter as tk

from visualenigma.config import DEFAULT_COLOR_SCHEME

class Plug(tk.Canvas):
    def __init__(self, plugboard, number, text):
        super().__init__(master=plugboard, width=30, height=30,
                         bd=1, highlightthickness=0, relief='raised',
                         bg=DEFAULT_COLOR_SCHEME['plug_int_top_inactive'])
        self.plugboard = plugboard
        self.number = number
        self.create_text(15, 15, fill='black', text=text, tags=('letter',))
        #self.sunken = False
        self.plugged_to = None
        self.bind('<ButtonPress-1>', self.on_press)

    def on_press(self, event):
        if self.number != None:
            self.plugboard.operate(self.number)


class PlugboardInterface(tk.Frame):

    def __init__(self, gui):
        super().__init__(master=gui, bg='white')
        self.gui = gui
        self.plugs = []
        self.sockets = []
        for i in range(len(self.gui.machine.alphabet)):
            self.plugs.append(Plug(self, i, self.gui.machine.alphabet[i]))
            self.plugs[i].grid(row=0, column=i)
            self.sockets.append(Plug(self, None, self.gui.machine.alphabet[i]))
            self.sockets[i].config(relief='flat', bg=DEFAULT_COLOR_SCHEME['plug_int_bottom_inactive'])
            self.sockets[i].grid(row=1, column=i)
        self.sunken = None
        print('        Plugboard interface initialized successfully.')

    def operate(self, i):
        if self.sunken == None:
            if self.plugs[i].plugged_to == None:
                self.plugs[i].config(relief='sunken', bg=DEFAULT_COLOR_SCHEME['plug_int_top_sunken'])
                self.sunken = i
            else:
                self.gui.machine.box.plugboard.swap(
                    i, self.plugs[i].plugged_to
                    )
                self.gui.box_int.plugboard_disp.update()
                self.sockets[i].config(bg=DEFAULT_COLOR_SCHEME['plug_int_bottom_inactive'])
                self.sockets[i].itemconfig(
                    'letter',
                    text=self.gui.machine.alphabet[i]
                    )
                self.sockets[self.plugs[i].plugged_to].config(bg=DEFAULT_COLOR_SCHEME['plug_int_bottom_inactive'])
                self.sockets[self.plugs[i].plugged_to].itemconfig(
                    'letter',
                    text=self.gui.machine.alphabet[self.plugs[i].plugged_to]
                    )
                self.plugs[self.plugs[i].plugged_to].config(bg=DEFAULT_COLOR_SCHEME['plug_int_top_inactive'])
                self.plugs[self.plugs[i].plugged_to].plugged_to = None
                self.plugs[i].config(bg=DEFAULT_COLOR_SCHEME['plug_int_top_inactive'])
                self.plugs[i].plugged_to = None
        elif self.sunken == i:
            self.plugs[i].config(relief='raised', bg=DEFAULT_COLOR_SCHEME['plug_int_top_inactive'])
            self.sunken = None
        else:
            if self.plugs[i].plugged_to != None:
                self.gui.machine.box.plugboard.swap(
                    i, self.plugs[i].plugged_to
                    )
                self.gui.box_int.plugboard_disp.update()
                self.sockets[i].config(bg=DEFAULT_COLOR_SCHEME['plug_int_bottom_inactive'])
                self.sockets[i].itemconfig(
                    'letter',
                    text=self.gui.machine.alphabet[i]
                    )
                self.sockets[self.plugs[i].plugged_to].config(bg=DEFAULT_COLOR_SCHEME['plug_int_bottom_inactive'])
                self.sockets[self.plugs[i].plugged_to].itemconfig(
                    'letter',
                    text=self.gui.machine.alphabet[self.plugs[i].plugged_to]
                    )
                self.plugs[self.plugs[i].plugged_to].config(bg=DEFAULT_COLOR_SCHEME['plug_int_top_inactive'])
                self.plugs[self.plugs[i].plugged_to].plugged_to = None
                self.plugs[i].config(bg=DEFAULT_COLOR_SCHEME['plug_int_top_inactive'])
                self.plugs[i].plugged_to = None
                self.sockets[i].itemconfig(
                    'letter',
                    text=self.gui.machine.alphabet[i]
                    )
            else:
                self.plugs[i].plugged_to = self.sunken
                self.plugs[i].config(relief='raised', bg=DEFAULT_COLOR_SCHEME['plug_int_top_active'])
                self.sockets[i].config(bg=DEFAULT_COLOR_SCHEME['plug_int_bottom_active'])
                self.sockets[i].itemconfig(
                    'letter',
                    text=self.gui.machine.alphabet[self.plugs[i].plugged_to]
                    )
                self.plugs[self.sunken].plugged_to = i
                self.plugs[self.sunken].config(relief='raised', bg=DEFAULT_COLOR_SCHEME['plug_int_top_active'])
                self.sockets[self.plugs[i].plugged_to].config(bg=DEFAULT_COLOR_SCHEME['plug_int_bottom_active'])
                self.sockets[self.plugs[i].plugged_to].itemconfig(
                    'letter',
                    text=self.gui.machine.alphabet[i]
                    )
                self.gui.machine.box.plugboard.swap(
                    i, self.plugs[i].plugged_to
                    )
                self.gui.box_int.plugboard_disp.update()
                self.sunken = None
        
        print('----------------')
        #print(self.sunken)
        for pair in self.gui.machine.box.plugboard.status:
            print(str(pair))
        print('----------------')
