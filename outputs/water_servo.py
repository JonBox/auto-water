class water_servo:
    def __init__(self, board):
        self.board = board

    def turn_on(self):
        self.board.turn_digital_output_on()

    def turn_off(self):
        self.board.turn_digital_output_off()

    def is_on(self):
        return self.board.digital_output_is_on()