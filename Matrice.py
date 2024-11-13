import machine
import neopixel

class Matrice:
    def __init__(self, led_pin, num_leds):
        self.led_pin = led_pin
        self.num_leds = num_leds
        self.np = neopixel.NeoPixel(machine.Pin(self.led_pin), self.num_leds)

    def set_color(self, index, color):
        if 0 <= index < self.num_leds:
            self.np[index] = color
            self.np.write()

    def clear_strip(self):
        for i in range(self.num_leds):
            self.np[i] = (0, 0, 0)
        self.np.write()

    def index_in_matrix(self, row, col):
        if col % 2 == 0:
            return col * 8 + row
        else:
            return col * 8 + (7 - row)

    def draw_snake(self, matrix, start_row, start_col):
        color = (0, 50, 0)
        rows = len(matrix)
        cols = len(matrix[0])
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 1:
                    index = self.index_in_matrix(start_row - r, start_col - c)
                    self.set_color(index, color)
        self.np.write()
