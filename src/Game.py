import random

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
                def make_lambda(param, which):
                    if which == 'right_click':
                        return lambda event: self.right_click(param)
                    elif which == 'left_click':
                        return lambda event: self.left_click(param)

                self.tile_list[(r, c)].button.bind('<Button-3>', make_lambda((r, c), 'right_click'))
                self.tile_list[(r, c)].button.bind('<Button-1>', make_lambda((r, c), 'left_click'))

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

    def left_click(self, position):
        """ Handles the left click event. """
        this_tile = self.tile_list[position]

        # if empty tile, then place a clue
        if this_tile.state == this_tile.states[0]:
            this_tile.state = this_tile.states[1]
            this_tile.show_clue(self.count_bombs(position))

        # if clue tile, then do nothing
        elif this_tile.state == this_tile.states[1]:
            return

        # if flag tile, then do nothing
        elif this_tile.state == this_tile.states[2][0] or this_tile.state == this_tile.states[2][1]:
            return

        # if bomb tile, then explode cutscene, end game.
        elif this_tile.state == this_tile.states[-1]:
            this_tile.show_bomb()

    def place_bomb(self, position):
        """ Changes the state of one tile to a bomb. position is tuple (posx, posy)"""
        this_tile = self.tile_list[position]
        this_tile.state = this_tile.states[-1]
        this_tile.show_empty()

    def place_random_bombs(self, amount):
        """ places [amount] random bombs onto the grid. """
        bombs = 0
        while bombs < amount:
            # randint is inclusive. Therefore, I do not want an x-coordinate of 10 if I have 10 rows.
            sample_x = random.randint(0, self.rows - 1)
            sample_y = random.randint(0, self.columns - 1)
            new_potential_bomb = self.tile_list[(sample_x, sample_y)]

            # if it's empty, place a bomb.
            if new_potential_bomb.state == Tile.states[0]:
                new_potential_bomb.state = Tile.states[-1]
                new_potential_bomb.show_empty()
                bombs += 1

    def clear_empties(self):
        """ This method should reveal each tile surrounding every 0 clue. """
        for this_tile in self.tile_list.values():
            # if it's a 0 clue, reveal all of it's surrounding.
            if this_tile.state == Tile.states[1] and this_tile.button['text'] == '  ':
                for this_surrounding in self.get_surrounding(this_tile.position):
                    self.left_click(this_surrounding)

    def get_surrounding(self, position):
        """ Returns a list of the legal, surrounding (including center) spaces. """
        surrounding = [
            (position[0] - 0, position[1] - 0),  # 5, 5
            (position[0] - 0, position[1] - 1),  # 5, 4
            (position[0] - 0, position[1] + 1),  # 5, 6
            (position[0] - 1, position[1] - 0),  # 4, 5
            (position[0] - 1, position[1] - 1),  # 4, 4
            (position[0] - 1, position[1] + 1),  # 4, 6
            (position[0] + 1, position[1] - 0),  # 5, 5
            (position[0] + 1, position[1] - 1),  # 5, 5
            (position[0] + 1, position[1] + 1),  # 5, 5
        ]
        legal_surrounding = []
        # only consider the legal spaces (not off the board)
        for space in surrounding:
            if space[0] in range(0, self.rows) and space[1] in range(0, self.columns):
                legal_surrounding.append(space)

        return legal_surrounding

    def count_bombs(self, position):
        """ Returns the amount of bombs in the eight surrounding spaces. """
        bombs = 0

        # count the bomb in each space
        for space in self.get_surrounding(position):

            # could be a bomb or a flagged bomb
            if self.tile_list[space].state == Tile.states[-1] or self.tile_list[space].state == Tile.states[2][1]:
                bombs += 1

        if bombs == 0:
            self.tile_list[position].button.config(text='  ')
            self.clear_empties()
            return '  '
        return bombs
