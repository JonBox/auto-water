from adafruit_ads1x15 import AnalogIn, ads1115
import board
import busio
import adafruit_ads1x15.ads1x15 as ADS

class moisture_sensor():
    def __init__(self):
        # Create sensor object, using the board's default I2C bus.
        self.i2c = busio.I2C(board.SCL, board.SDA)  # uses board.SCL and board.SDA
        self.ads = ads1115.ADS1115(self.i2c)
        self.chan = AnalogIn(self.ads, ADS.Pin.A0)
    def get_moisture_level(self):
        return (self.chan.value, self.chan.voltage)