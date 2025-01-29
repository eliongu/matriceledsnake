from game import *
from buzzer import *

class Main:
    def __init__(self):
        self.game = Game()

    def run(self):
        self.game.game()



if __name__ == '__main__':
    main = Main()
    main.run()
