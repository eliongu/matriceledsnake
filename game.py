from Matrice import *
from Snake import *
from button import *

snake = Snake(matrice=[[1]], x=1, y=1)
bup = Button(9)
bdown = Button(2)
bright = Button(3)
bleft = Button(8)
matrice = Matrice(led_pin=10, num_leds=64)

game = 0

while game == 1:
    matrice.draw_snake(snake._matrice, snake.getx(), snake.gety())
    if (bup.get_value() == 1):
        snake.move_up()
        matrice.clear_strip()

    if (bdown.get_value() == 1):
        snake.move_down()
        matrice.clear_strip()

    if (bright.get_value() == 1):
        snake.move_right()
        matrice.clear_strip()

    if (bleft.get_value() == 1):
        snake.move_left()
        matrice.clear_strip()
    snake.is_out_of_bounds()
    matrice.draw_snake(snake._matrice, snake.getx(), snake.gety())
