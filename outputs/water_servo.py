#https://learn.adafruit.com/circuitpython-on-any-computer-with-ft232h/running-circuitpython-code-without-circuitpython
#from pyftdi.ftdi import Ftdi
#Ftdi().open_from_url('ftdi:///?')

import board
import digitalio


class water_servo:
    def __init__(self):
        self.water = digitalio.DigitalInOut(board.C0)
        self.water.direction = digitalio.Direction.OUTPUT

    def turn_on(self):
        self.water.value = True

    def turn_off(self):
        self.water.value = False

    def is_on(self):
        return self.water.value