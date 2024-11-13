import random

class fruit:
    def __init__(self, matrice, x, y,color):
        self._matrice = matrice
        self._x = x
        self._y = y
        self._color = ()#green

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def gety(self):
        return self._y

    def sety(self, value):
        self._y = value

    def randomint(self, positionlist):
        while True:
            randx = random.randint(0,7)
            randy = random.randint(0,7)
            if (randx or randy) not in positionlist:
                return randx, randy