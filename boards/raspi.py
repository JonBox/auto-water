from boards.hardware import hardware
from gpiozero import OutputDevice
from adafruit_ads1x15 import AnalogIn, ads1115
import busio
import adafruit_ads1x15.ads1x15 as ADS
import board


class raspi(hardware):
    def __init__(self):
        self.i2c = busio.I2C(board.SCL, board.SDA)  # uses board.SCL and board.SDA
        self.ads = ads1115.ADS1115(self.i2c)
        self.chan = AnalogIn(self.ads, ADS.Pin.A0)
        self.output = OutputDevice(5, active_high=True)
    def get_analog_input(self):
        return self.chan.value, self.chan.voltage
    def turn_digital_output_on(self):
        self.output.on()
    def turn_digital_output_off(self):
        self.output.off()
    def digital_output_is_on(self):
        return self.output.value