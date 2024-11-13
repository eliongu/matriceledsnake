import machine

class Button:
    bup = machine.Pin(9, machine.Pin.OUT, machine.Pin.PULL_UP)
    bdown = machine.Pin(2, machine.Pin.OUT, machine.Pin.PULL_UP)
    bright = machine.Pin(3, machine.Pin.OUT, machine.Pin.PULL_UP)
    bleft = machine.Pin(8, machine.Pin.OUT, machine.Pin.PULL_UP)
    def __init__(self):
