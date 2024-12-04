from Matrice import *
from Snake import *
from button import *
from fruit import *
import time


def randomint(positionlist):
    while True:
        randx = random.randint(0, 7)
        randy = random.randint(0, 7)
        if (randx, randy) not in positionlist:
            return randx, randy

def eat(sx, sy, fx, fy):
    return sx == fx and sy == fy


def game():
    snake = Snake(matrice=[[1]], x=0, y=0, color=(0, 10, 0), direction="RIGHT")
    matrice = Matrice(led_pin=10, num_leds=64)
    fruit = Fruit(matrice=[[1]], x=4, y=4, color=(10, 2, 2))
    positionlist = [(snake.getx(), snake.gety())]

    bup = Button(7)
    bdown = Button(3)
    bright = Button(2)
    bleft = Button(9)

    stop = False

    while not stop:
        matrice.clear_strip()

        for segment in positionlist:
            matrice.draw(snake._matrice, segment[0], segment[1], snake._color)

        matrice.draw(fruit._matrice, fruit.getx(), fruit.gety(), fruit._color)

        if eat(snake.getx(), snake.gety(), fruit.getx(), fruit.gety()):
            fx, fy = randomint(positionlist)
            fruit.setx(fx)
            fruit.sety(fy)
            positionlist.append(positionlist[-1])


        if bup.get_value() == 1:
            snake.set_direction("UP")
        elif bdown.get_value() == 1:
            snake.set_direction("DOWN")
        elif bright.get_value() == 1:
            snake.set_direction("RIGHT")
        elif bleft.get_value() == 1:
            snake.set_direction("LEFT")

        new_head = (snake.getx(), snake.gety())
        positionlist = [new_head] + positionlist[:-1]

        if positionlist.length() < 5:
            for segment in positionlist:
                if snake.getx() == segment[2] and snake.gety() == segment[3]:
                    Matrice.slide(matrice, LOSER, 1, 3)
                    print("Loser")
                    stop = True

        if snake.get_direction() == "UP":
            snake.move_up()
        elif snake.get_direction() == "DOWN":
            snake.move_down()
        elif snake.get_direction() == "RIGHT":
            snake.move_right()
        elif snake.get_direction() == "LEFT":
            snake.move_left()

        snake.is_out_of_bounds()
        time.sleep(0.7)
