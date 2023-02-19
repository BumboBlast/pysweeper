from Game import *

root = Tk()
root.title('John Minesweeper')
root.bind('<Escape>', lambda event: root.destroy())

game = Game(10, 10)

game.add_bomb((1, 1))
game.add_bomb((2, 1))
game.add_bomb((7, 8))

print(game.count_bombs((1, 2)))

# opens the window
root.mainloop()
