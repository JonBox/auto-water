from datetime import datetime, timedelta


class water_servo:
    def __init__(self, board):
        self.board = board
        self.watering_time = 60*15 # 15min
        self.watering_started_at = datetime.now()
        self.watering_ends_at = None

    def turn_on(self, watering_time = None):
        print(f"Watering for {watering_time} seconds")
        self.board.turn_digital_output_on()
        self.watering_started_at = datetime.now()
        self.watering_ends_at = self.watering_started_at + timedelta(seconds=watering_time)

    def turn_off(self):
        print(f"Watering stopped")
        self.board.turn_digital_output_off()

    def is_on(self):
        return self.board.digital_output_is_on()

    def auto_off(self):
        self.watering_started_at = datetime.now()
        if self.board.digital_output_is_on() and self.watering_ends_at < datetime.now():
            print(f"Auto-off triggered")
            self.board.turn_digital_output_off()