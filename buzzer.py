from machine import Pin, PWM
import time

class Buzzer:
    def __init__(self, pin_number=8):
        self.buzzer_pin = Pin(pin_number, Pin.OUT)
        self.pwm = PWM(self.buzzer_pin)

        self.melody = [330, 392, 440, 392, 330, 262, 294, 330]  # Mi, Sol, La, Sol, Mi, Do, Ré, Mi
        self.note_durations = [200, 200, 200, 200, 400, 200, 200, 400]  # Durée de chaque note en ms

    def play_intro(self):
        for i in range(len(self.melody)):
            self.pwm.freq(self.melody[i])
            self.pwm.duty(512)
            time.sleep(self.note_durations[i] / 1000)
            self.pwm.duty(0)
            time.sleep(0.05)
