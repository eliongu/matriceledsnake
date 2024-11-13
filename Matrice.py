import machine
import neopixel

LED_PIN = 10
NUM_LEDS = 64
np = neopixel.NeoPixel(machine.Pin(LED_PIN), NUM_LEDS)


def set_color(index, color):
    if 0 <= index < NUM_LEDS:
        np[index] = color
        np.write()


def clear_strip():
    for i in range(NUM_LEDS):
        np[i] = (0, 0, 0)
        np.write()


def index_in_matrix(row, col):
    if col % 2 == 0:
        return col * 8 + row
    else:
        return col * 8 + (7 - row)


def draw_snake(matrix, start_row, start_col):
    color = (0, 50, 0)
    rows = len(matrix)
    cols = len(matrix[0])
    if start_row > 7:
        diff = start_row - 7
        cols -= diff
    if start_col > 7:
        dif = start_col - 7
        rows -= dif
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1:
                index = index_in_matrix(start_row - r, start_col - c)
                set_color(index, color)
    np.write()


