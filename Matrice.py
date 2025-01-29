import machine
import neopixel
import time

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

    def draw(self, matrix, start_row, start_col,color):
        rows = len(matrix)
        cols = len(matrix[0])
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 1:
                    index = self.index_in_matrix(start_row - r, start_col - c)
                    self.set_color(index, color)
        self.np.write()

    def wheel(self, pos):
        if pos < 85:
            return (pos * 3, 255 - pos * 3, 0)
        elif pos < 170:
            pos -= 85
            return (255 - pos * 3, 0, pos * 3)
        else:
            pos -= 170
            return (0, pos * 3, 255 - pos * 3)

    def slide(self,matrix, start_row, wait, colorfull):
        rows = len(matrix)
        cols = len(matrix[0])

        for offset in range(-15, cols):
            self.clear_strip()
            for r in range(8):
                for c in range(16):
                    matrix_col = c + offset
                    if 0 <= matrix_col < cols and 0 <= start_row + r < rows:
                        if matrix[start_row + r][matrix_col] == 1:
                            if colorfull:
                                color = self.wheel((r * 16 + c) & 255)
                            else :
                                color = (10, 10, 10)
                            index = self.index_in_matrix(r, c)
                            self.set_color(index, color)
            self.np.write()
            time.sleep_ms(wait)
        self.clear_strip()


LOSER = [
    [0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0],
    [1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0],
    [1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1]
]