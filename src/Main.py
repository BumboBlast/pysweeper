from Game import *

root = Tk()
root.title('John Minesweeper')
root.bind('<Escape>', lambda kill: root.destroy())

number_rows = 10
number_columns = 15
game = Game(number_rows, number_columns)

game.place_random_bombs(10)

# opens the window
root.mainloop()
