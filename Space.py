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
        self.button.bind('<Leave>', lambda event: self.raise_button())

        self.state = self.states[0]
        self.position = (posx, posy)

        # address to the game class
        self.game_handle = game

    def raise_button(self):
        """ Shows the button as raised when cursor leave. Only if empty or bomb. """
        if self.state == self.states[0] or self.state == self.states[3]:
            self.button.config(relief='raised')

    def sink_button(self):
        """ Shows the button as depressed when mouse over, if empty or a bomb. """
        if self.state == self.states[0] or self.state == self.states[3]:
            self.button.config(relief='groove')

    def right_click(self):
        """ Handles the case the user right-clicks the button. """
        # place a flag
        if self.state == self.states[0] or self.state == self.states[3]:
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

        # if this is first click of the game
        if self.game_handle.first_click:
            self.game_handle.first_click = False
            empty_spaces = self.game_handle.place_random_mines(self.position)
            print(empty_spaces)

            # clear some spaces around click
            for pos in empty_spaces:
                space = self.game_handle.space_list[pos]
                space.state = space.states[2]
                space.button.config(state='disabled')
                space.button.config(relief='sunken')
                space.button.config(bg='#e1dad8')
                space.button.config(text=space.game_handle.count_bombs(pos))

        # place a clue if empty
        elif self.state == self.states[0]:
            self.state = self.states[2]
            self.button.config(state='disabled')
            self.button.config(relief='sunken')
            self.button.config(bg='#e1dad8')
            self.button.config(text=self.game_handle.count_bombs(self.position))

        # explode if a bomb
        elif self.state == self.states[3]:
            self.button.config(state='disabled')
            self.button.config(text='bomb')
            # end cutscene
