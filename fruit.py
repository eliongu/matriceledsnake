import random

class Fruit:
    def __init__(self, matrice, x, y, color):
        self._matrice = matrice
        self._x = x
        self._y = y
        self._color = color

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def gety(self):
        return self._y

    def sety(self, value):
        self._y = value