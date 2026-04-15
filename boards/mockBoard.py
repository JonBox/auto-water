import random

from boards.hardware import hardware


class mockBoard(hardware):
    def __init__(self):
        self.water = False
    def get_analog_input(self):
        return {'sensor1': random.randrange(0,10000, 1)/10000}
    def turn_digital_output_on(self):
        self.water = True
    def turn_digital_output_off(self):
        self.water = False
    def digital_output_is_on(self):
        return self.water