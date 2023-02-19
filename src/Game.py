from Tile import *

""" Implements methods that affect the game state. """


class Game:

    def __init__(self, rows, columns):
        """ Makes a new game with the parameter's number of rows/ columns. """
        self.rows = rows
        self.columns = columns

        self.tile_list = {}

        # put the buttons on a grid
        for r in range(rows):
            for c in range(columns):
                self.tile_list[(r, c)] = Tile(r, c)
                self.tile_list[(r, c)].button.grid(row=r, column=c)

                # give each button a bind
                def make_lambda(x):
                    return lambda event: self.right_click(x)
                self.tile_list[(r, c)].button.bind('<Button-3>', make_lambda((r, c)))

    def right_click(self, position):
        """ Handles the right click event. """
        this_tile = self.tile_list[position]

        # if empty, set to empty_flag
        if this_tile.state == this_tile.states[0]:
            this_tile.state = this_tile.states[2][0]
            this_tile.show_flag()

        # if bomb, set to bomb_flag
        elif this_tile.state == this_tile.states[-1]:
            this_tile.state = this_tile.states[2][1]
            this_tile.show_flag()

        # if flag_empty, then remove flag
        elif this_tile.state == this_tile.states[2][0]:
            this_tile.state = this_tile.states[0]
            this_tile.show_empty()

        # if flag_bomb, then remove flag
        elif this_tile.state == this_tile.states[2][1]:
            this_tile.state = this_tile.states[-1]
            this_tile.show_empty()

    def place_bomb(self, position):
        """ Changes the state of one tile to a bomb. position is tuple (posx, posy)"""
        this_tile = self.tile_list[position]
        this_tile.state = this_tile.states[-1]
        this_tile.show_empty()
