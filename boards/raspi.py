from boards.hardware import hardware
from gpiozero import OutputDevice

class raspi(hardware):
    self.output = OutputDevice(5, active_high=False)
    def __init__(self):
        pass
    def get_analog_input(self):
        return None
    def turn_digital_output_on(self):
        self.output.on()
    def turn_digital_output_off(self):
        self.output.off()
    def digital_output_is_on(self):
        return self.output.value