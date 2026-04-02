
def get_board():
    try:
        from boards.ft232 import ft232
        return ft232()
    except (ValueError, ImportError, Excetion) as e:
        pass

    try:
        from boards.raspi import raspi
        return raspi()
    except ImportError:
        pass

    raise RuntimeError("No compatible board implementation found for this platform")