from tkinter import *

""" implements methods that affect the Tile Object. """


class Tile:
    states = ['empty', 'clue', ['flag_empty', 'flag_bomb'], 'bomb']
    empty = {
        'text': ' ',
        'color': '#FFD9DF'
    }
    flag = {
        'text': 'flag',
        'color': '#FFC0CB'
    }

    def __init__(self, posx, posy):
        """ A Tile is a button with metadata. """
        self.position = (posx, posy)
        self.button = Button(height=3, width=6, bg=self.empty['color'])
        self.button.bind('<Enter>', lambda event: self.select_button())
        self.button.bind('<Leave>', lambda event: self.deselect_button())
        self.button.bind('<Button-3>', lambda event: self.right_click())

        # each tile starts out as empty
        self.state = self.states[0]

    def select_button(self):
        """ Button only reacts to cursor if its not been clicked on (empty or bomb) """
        if self.state == self.states[0] or self.state == self.states[-1]:
            self.button.config(relief='solid')

    def deselect_button(self):
        """ Button only reacts to cursor if its not been clicked on (empty or bomb) """
        if self.state == self.states[0] or self.state == self.states[-1]:
            self.button.config(relief='raised')

    def right_click(self):
        """ Handles the right click event. """
        # if empty, set to empty_flag
        if self.state == self.states[0]:
            self.state = self.states[2][0]
            self.button.config(relief='raised')
            self.button.config(bg=self.flag['color'])
            self.button.config(text=self.flag['text'])

        # if bomb, set to bomb_flag
        elif self.state == self.states[-1]:
            self.state = self.states[2][1]
            self.button.config(relief='raised')
            self.button.config(bg=self.flag['color'])
            self.button.config(text=self.flag['text'])

        # if flag_empty, then remove flag
        elif self.state == self.states[2][0]:
            self.state = self.states[0]
            self.button.config(bg=self.empty['color'])
            self.button.config(text=self.empty['text'])

        # if flag_bomb, then remove flag
        elif self.state == self.states[2][1]:
            self.state = self.states[-1]
            self.button.config(bg=self.empty['color'])
            self.button.config(text=self.empty['text'])
