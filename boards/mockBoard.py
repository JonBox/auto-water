import random

from boards.hardware import hardware


class mockBoard(hardware):
    def __init__(self):
        pass
    def get_analog_input(self):
        return {'sensor1': random.randrange(0,1)}
    def turn_digital_output_on(self):
        pass
    def turn_digital_output_off(self):
        pass
    def digital_output_is_on(self):
        return False