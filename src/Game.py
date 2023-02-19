from tkinter import *
from Tile import *

""" Implements methods that affect the game state. """


class Game:

    def __init__(self, rows, columns):
        """ Makes a new game with the parameter's number of rows/ columns. """
        self.rows = rows
        self.columns = columns

        for r in range(rows):
            for c in range(columns):
                new_tile = Tile(r, c)
                new_tile.button.grid(row=r, column=c)
