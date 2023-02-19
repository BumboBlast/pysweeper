from tkinter import *

""" implements methods that affect the Tile Object. """


class Tile:
    states = ['empty', 'clue', ['flag_empty', 'flag_bomb'], 'bomb']
    empty = {
        'text': '',
        'color': '#FFD9DF'
    }
    clue = {
        'text': '',
        'color': '#BFFFCB'
    }
    flag = {
        'text': '🚩',
        'color': '#FFC0CB'
    }
    bomb = {
        'text': 'bomb',
        'color': 'red'
    }

    def __init__(self, posx, posy):
        """ A Tile is a button with metadata. """
        self.position = (posx, posy)
        self.button = Button(height=3, width=6, bg=self.empty['color'])
        self.button.bind('<Enter>', lambda event: self.highlight_tile())
        self.button.bind('<Leave>', lambda event: self.de_highlight_tile())

        # each tile starts out as empty
        self.state = self.states[0]

    def highlight_tile(self):
        """ Button only reacts to cursor if it's not been clicked on (empty or bomb) """
        if self.state == self.states[0] or self.state == self.states[-1]:
            self.button.config(relief='solid')

    def de_highlight_tile(self):
        """ Button only reacts to cursor if it's not been clicked on (empty or bomb) """
        if self.state == self.states[0] or self.state == self.states[-1]:
            self.button.config(relief='raised')

    def show_empty(self):
        """ Change how this tile looks to being empty (or a bomb). """
        self.button.config(relief='raised')
        self.button.config(state='normal')
        self.button.config(bg=self.empty['color'])
        self.button.config(text=self.empty['text'])

    def show_clue(self, clue_number):
        """ Change how this tile looks to being a clue. """
        self.button.config(relief='raised')
        self.button.config(state='disabled')
        self.button.config(bg=self.clue['color'])
        self.button.config(text=str(clue_number))  # how many surrounding bombs

    def show_flag(self):
        """ Change how this tile looks to being a flag. """
        self.button.config(relief='raised')
        self.button.config(state='disabled')
        self.button.config(bg=self.flag['color'])
        self.button.config(text=self.flag['text'])

    def show_bomb(self):
        """ Change how this tile looks to being a bomb. """
        self.button.config(relief='raised')
        self.button.config(state='disabled')
        self.button.config(bg=self.bomb['color'])
        self.button.config(text=self.bomb['text'])
