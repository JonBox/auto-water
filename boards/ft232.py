from boards.hardware import hardware
from adafruit_ads1x15 import AnalogIn, ads1115
import busio
import adafruit_ads1x15.ads1x15 as ADS
import board
import digitalio

class ft232(hardware):
    def __init__(self):
        self.i2c = busio.I2C(board.SCL, board.SDA)  # uses board.SCL and board.SDA
        self.ads = ads1115.ADS1115(self.i2c)
        self.chan = AnalogIn(self.ads, ADS.Pin.A0)
        self.digital = digitalio.DigitalInOut(board.C0)
        self.digital.direction = digitalio.Direction.OUTPUT
    def get_analog_input(self):
        return { 'sensor1':  self.chan.voltage }
    def turn_digital_output_on(self):
        self.digital.value = True
    def turn_digital_output_off(self):
        self.digital.value = False
    def digital_output_is_on(self):
        return self.digital.value