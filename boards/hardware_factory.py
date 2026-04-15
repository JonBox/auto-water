import os


def get_board():
    if os.environ.get('board') == "mock":
        from boards.mockBoard import mockBoard
        return mockBoard()
    try:
        from boards.ft232 import ft232
        return ft232()
    except (ValueError, ImportError, Exception) as e:
        pass

    try:
        from boards.raspi import raspi
        return raspi()
    except ImportError:
        pass

    raise RuntimeError("No compatible board implementation found for this platform")