class moisture_sensor():
    def __init__(self, board):
        self.board = board
    def get_moisture_level(self):
        return self.board.get_analog_input()