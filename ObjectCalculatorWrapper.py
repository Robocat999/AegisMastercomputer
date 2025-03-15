class ObjectCalculatorWrapper:
    """
    Wraps up the value based calculator so that it can be interfaced with plane machines instead of numbers
    """

    def __init__(self):
        self.plane = None

        self.stick_position = 0
        self.throttle_position = 0
        self.yaw_position = 0

