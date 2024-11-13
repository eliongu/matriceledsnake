import time
from Snake import *
from Matrice import *
from button import *

snake = Snake(matrice=[[1]], x=1, y=1)

game = 0

while game == 0:
    draw_snake(snake._matrice, snake.getx(), snake.gety())

    while True:
        if bup.value() == 1:
            snake.setx(snake.getx() + 1)
            clear_strip()
        print(bup.value())
        if bdown.value() == 1:
            print(bdown.value())
            snake.setx(snake.getx() - 1)
            clear_strip()
        if bright.value() == 1:
            print(bright.value())
            snake.sety(snake.gety() - 1)
            clear_strip()
        if bleft.value() == 1:
            print(bleft.value())
            snake.sety(snake.gety() + 1)
            clear_strip()
        Snake.is_out_of_bounds(snake)
        draw_snake(snake._matrice, snake.getx(), snake.gety())

        time.sleep(0.1)

