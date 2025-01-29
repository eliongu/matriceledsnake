from button import *

class Snake:

    def __init__(self, matrice, x, y, color, direction):
        self.matrice = matrice
        self.x = x
        self.y = y
        self.color = color
        self.direction = direction
        self.bup = Button(2)
        self.bdown = Button(3)
        self.bright = Button(7)
        self.bleft = Button(9)


    def move_up(self):
        self.y += 1

    def move_down(self):
        self.y -= 1

    def move_right(self):
        self.x += 1

    def move_left(self):
        self.x -= 1

    def movement(self):
        if self.direction == "UP":
            self.move_up()
        elif self.direction == "DOWN":
            self.move_down()
        elif self.direction == "RIGHT":
            self.move_right()
        elif self.direction == "LEFT":
            self.move_left()

    def condition(self):
        if self.bup.get_value() == 1:
            self.direction = "UP"
        elif self.bdown.get_value() == 1:
            self.direction = "DOWN"
        elif self.bright.get_value() == 1:
            self.direction = "RIGHT"
        elif self.bleft.get_value() == 1:
            self.direction = "LEFT"


    def is_out_of_bounds(self):
        if (self.x > 7):
            self.x = 0
        if (self.y > 7):
            self.y = 0
        if (self.x < 0):
            self.x = 7
        if (self.y < 0):
            self.y = 7