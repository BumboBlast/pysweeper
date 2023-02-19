from tkinter import *
from Game import *


class Space:
    """ Provides methods to what the buttons do. """

    states = ['empty', 'flag', 'clue', 'bomb']

    def __init__(self, button_height, button_width, posx, posy, game):
        self.button = Button(height=button_height, width=button_width)
        self.button.bind('<Button-3>', lambda event: self.right_click())
        self.button.bind('<Button-1>', lambda event: self.left_click())
        self.button.bind('<Enter>', lambda event: self.sink_button())
        self.button.bind('<Leave>', lambda event: self.button.config(relief='raised'))

        self.state = self.states[0]
        self.position = (posx, posy)
        self.game_state = game

    def sink_button(self):
        """ Shows the button as depressed when mouse over, if empty or a bomb. """
        if self.state == self.states[0] or self.state == self.states[3]:
            self.button.config(relief='groove')

    def right_click(self):
        """ Handles the case the user right-clicks the button. """
        # place a flag
        if self.state == self.states[0]:
            self.state = self.states[1]
            self.button.config(state='disabled')
            self.button.config(text='🚩')

        # remove the flag
        elif self.state == self.states[1]:
            self.state = self.states[0]
            self.button.config(state='normal')
            self.button.config(text='')

    def left_click(self):
        """ Handles the case the user left-clicks the button. """
        # place a clue if empty
        if self.state == self.states[0]:
            self.state = self.states[2]
            self.button.config(state='disabled')
            self.button.config(text=self.game_state.count_bombs(self.position))

        # explode if a bomb
        elif self.state == self.states[3]:
            self.button.config(state='disabled')
            self.button.config(text='bomb')
            # end cutscene
