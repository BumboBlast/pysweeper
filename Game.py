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

        self.first_click = True

    def add_bomb(self, position):
        """ Mark the space in the passed position as a bomb. """
        space = self.space_list[position]
        space.state = Space.states[-1]

    def count_bombs(self, position):
        """ returns the amount of bombs in the surrounding 8 spaces. """
        bombs = 0
        for space in self.get_surrounding(position):
            # if this space is a bomb
            if self.space_list[space].state == Space.states[-1]:
                bombs += 1

        # open up all the spaces surrounding it.
        if bombs == 0:
            return ' '

        return bombs

    def place_random_mines(self, start_position):
        # ~ 10 percent are bombs
        # pick 10 percent random spots

        # reserve the surrounding spaces to the first click
        reserved = self.get_surrounding(start_position)

        # place 10% grid size amount of random bombs, not in reserved spot.
        for r in range(0, int(self.rows * self.columns * 0.2)):
            sample_x = random.randrange(self.rows)
            sample_y = random.randrange(self.columns)
            if (sample_x, sample_y) not in reserved:  # should re roll instead
                self.add_bomb((sample_x, sample_y))

        # return the list of positions that are not bombs

        return reserved

    def get_surrounding(self, position):
        """ return the list of adjacent  spaces. First element is center. """
        surrounding = [
            (position[0] - 0, position[1] - 0),  # 5, 5
            (position[0] - 0, position[1] - 1),  # 5, 4
            (position[0] - 0, position[1] + 1),  # 5, 6
            (position[0] - 1, position[1] - 0),  # 4, 5
            (position[0] - 1, position[1] - 1),  # 4, 4
            (position[0] - 1, position[1] + 1),  # 4, 6
            (position[0] + 1, position[1] - 0),  # 6, 5
            (position[0] + 1, position[1] - 1),  # 6, 4
            (position[0] + 1, position[1] + 1),  # 6, 6
        ]

        legal_surrounding = []
        for space in surrounding:
            # if this space is on the board
            if space[0] in range(0, self.rows) and space[1] in range(0, self.columns):
                legal_surrounding.append(space)

        return legal_surrounding

    def clear_all_empties(self):
        """ Iterate through all the 0's. Clear all their surrounding spaces. """
        for space in self.space_list.values():
            # if it's a clue and a 0
            if space.state == space.states[1] and space.button['text'] == ' ':
                for surrounding_position in self.get_surrounding(space.position):
                    surrounding_space = self.space_list[surrounding_position]
                    surrounding_space.state = Space.states[1]
                    surrounding_space.button.config(state='disabled')
                    surrounding_space.button.config(relief='sunken')
                    surrounding_space.button.config(bg='#e1dad8')
                    surrounding_space.button.config(text=self.count_bombs(surrounding_position))

