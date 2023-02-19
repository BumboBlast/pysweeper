import random
from Space import *


class Game:
    """ methods that control the state of the game as a whole. """

    def __init__(self, amount_rows, amount_columns):
        self.space_list = {}

        self.rows = amount_rows
        self.columns = amount_columns

        # append grid of buttons to a dictionary
        for rows in range(0, amount_rows):
            for columns in range(0, amount_columns):
                new_button = Space(3, 6, rows, columns, self)
                new_button.button.grid(row=rows, column=columns)
                self.space_list[new_button.position] = new_button

    def add_bomb(self, position):
        """ Mark the space in the passed position as a bomb. """
        space = self.space_list[position]
        space.state = space.states[3]
        space.button.config(state='disabled')

    def count_bombs(self, position):
        """ returns the amount of bombs in the surrounding 8 spaces. """
        surrounding = [
            # (position[0] - 0, position[1] - 0),  # 5, 5
            (position[0] - 0, position[1] - 1),  # 5, 4
            (position[0] - 0, position[1] + 1),  # 5, 6
            (position[0] - 1, position[1] - 0),  # 4, 5
            (position[0] - 1, position[1] - 1),  # 4, 4
            (position[0] - 1, position[1] + 1),  # 4, 6
            (position[0] + 1, position[1] - 0),  # 6, 5
            (position[0] + 1, position[1] - 1),  # 6, 4
            (position[0] + 1, position[1] + 1),  # 6, 6
        ]

        bombs = 0
        for space in surrounding:
            # if this space is a bomb
            if space[0] in range(0, self.rows) and space[1] in range(0, self.columns):
                if self.space_list[space].state == Space.states[3]:
                    bombs += 1
        return bombs

    def place_random_mines(self, reserved):
        # ~ 10 percent are bombs
        # pick 10 percent random spots
        for r in range(0, int(self.rows * self.columns * 0.1)):
            sample_x = random.randrange(self.rows)
            sample_y = random.randrange(self.columns)
            if sample_x not in reserved and sample_y not in reserved:
                self.add_bomb((sample_x, sample_y))

    def get_adjacent_empties(self):
        """ return a list of adjacent (not diagonal) positions to spaces that are empty. """
