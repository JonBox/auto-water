from datetime import datetime, timedelta


class water_servo:
    def __init__(self, board):
        self.board = board
        self.watering_time = 60*1 # 15min
        self.watering_started_at = datetime.now()

    def turn_on(self):
        self.board.turn_digital_output_on()
        self.watering_started_at = datetime.now()

    def turn_off(self):
        self.board.turn_digital_output_off()

    def is_on(self):
        return self.board.digital_output_is_on()

    def auto_off(self):
        if self.board.digital_output_is_on() and self.watering_started_at < (datetime.now() - timedelta(seconds=self.watering_time)):
            self.board.turn_digital_output_off()

