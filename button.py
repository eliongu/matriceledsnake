import machine

class Button:
    def __init__(self, pin_number):
        self.button_pin = machine.Pin(pin_number, machine.Pin.IN, machine.Pin.PULL_DOWN)

    def get_value(self):
        return self.button_pin.value()
