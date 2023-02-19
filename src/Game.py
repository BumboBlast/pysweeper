from Tile import *

""" Implements methods that affect the game state. """


class Game:

    def __init__(self, rows, columns):
        """ Makes a new game with the parameter's number of rows/ columns. """
        self.rows = rows
        self.columns = columns

        self.tile_list = {}

        for r in range(rows):
            for c in range(columns):
                new_tile = Tile(r, c)
                new_tile.button.grid(row=r, column=c)
                self.tile_list[new_tile.position] = new_tile

    def place_bomb(self, position):
        """ Changes the state of one tile to a bomb. position is tuple (posx, posy)"""
        this_tile = self.tile_list[position]
        this_tile.state = this_tile.states[-1]
        this_tile.show_empty()
