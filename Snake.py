class Snake:
    def __init__(self, matrice=[[1]], x=1, y=1):
        self._matrice = matrice
        self._x = x
        self._y = y

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def gety(self):
        return self._y

    def sety(self, value):
        self._y = value

    def move_up(self):
        self.sety(self.gety() + 1)

    def move_down(self):
        self.sety(self.gety() - 1)

    def move_right(self):
        self.setx(self.getx() + 1)

    def move_left(self):
        self.setx(self.getx() - 1)

    def is_out_of_bounds(self):
        if (self.getx() > 7):
            self.setx(self.getx() - 7)
        if (self.gety() > 7):
            self.sety(self.gety() - 7)
        if (self.getx() < 0):
            self.setx(self.getx() + 7)
        if (self.gety() < 0):
            self.sety(self.gety() + 7)


