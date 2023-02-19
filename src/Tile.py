from tkinter import *

""" implements methods that affect the Tile Object. """


class Tile:

    states = ['empty', 'clue', ['flag_empty', 'flag_bomb'], 'bomb']

    def __init__(self, posx, posy):
        """ A Tile is a button with metadata. """
        self.position = (posx, posy)
        self.button = Button(height=3, width=6)
        self.button.bind('<Enter>', lambda event: self.select_button())
        self.button.bind('<Leave>', lambda event: self.deselect_button())

    def select_button(self):
        self.button.config(relief='solid')

    def deselect_button(self):
        self.button.config(relief='raised')
