class Snake:
    def __init__(self, matrice, x, y, color, direction):
        self._matrice = matrice
        self._x = x
        self._y = y
        self._color = color
        self._direction = direction

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def gety(self):
        return self._y

    def sety(self, value):
        self._y = value

    def get_direction(self):
        return self._direction

    def set_direction(self, value):
        self._direction = value

    def move_up(self):
        self.sety(self.gety() + 1)

    def move_down(self):
        self.sety(self.gety() - 1)

    def move_right(self):
        self.setx(self.getx() + 1)

    def move_left(self):
        self.setx(self.getx() - 1)

    def is_out_of_bounds(self):
        x = self.getx()
        y = self.gety()
        if (x > 7):
            self.setx(x - 7)
        if (y > 7):
            self.sety(y- 7)
        if (x < 0):
            self.setx(x + 7)
        if (y < 0):
            self.sety(y + 7)






