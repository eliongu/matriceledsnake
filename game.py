from Matrice import *
from Snake import *
from buzzer import *
from fruit import *
import time

class Game :
    def __init__(self) :
        self.matrice = Matrice(10, 64)
        self.snake = Snake([[1]], 0, 0, (0, 10, 0), "RIGHT")
        self.fruit = Fruit([[1]], 4, 4, (10, 2, 2))
        self.positionlist = [(self.snake.x, self.snake.y)]
        self.buzzer = Buzzer()

    def randomint(self, positionlist):
        while True:
            randx = random.randint(0, 7)
            randy = random.randint(0, 7)
            if (randx, randy) not in positionlist:
                return randx, randy

    def eat(self, sx, sy, fx, fy):
        return sx == fx and sy == fy

    def game(self):
        snake = self.snake
        fruit = self.fruit
        matrice = self.matrice
        stop = False
        self.buzzer.play_intro()

        while not stop:
            matrice.clear_strip()

            for segment in self.positionlist:
                matrice.draw(snake.matrice, segment[0], segment[1], snake.color)

            matrice.draw(fruit.matrice, fruit.x, fruit.y, fruit.color)

            if self.eat(snake.x, snake.y, fruit.x, fruit.y):
                fx, fy = self.randomint(self.positionlist)
                fruit.x = fx
                fruit.y = fy
                self.positionlist.append(self.positionlist[-1])

            snake.condition()   #check la valeur du bouton
            snake.movement()    #redirige le serpent en fonction de la valeur des boutons

            if len(self.positionlist) > 1:
                for segment in self.positionlist[1:]:
                    if (snake.x, snake.y) == segment:
                        Matrice.slide(matrice, LOSER, -1, 70, colorfull=False)
                        stop = True

            new_head = (snake.x, snake.y)
            self.positionlist = [new_head] + self.positionlist[:-1]


            snake.is_out_of_bounds()
            time.sleep(0.7)
