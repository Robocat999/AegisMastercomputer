class ValueBasedCalculator:
    """
    Makes predictions based off of plane values
    """

    def __init__(self):
        self.plane = None
        self.maneuver_airspeed = 0

        self.pitch_change = 0
        self.roll_change = 0
        self.heading_change = 0
        self.airspeed_change = 0
        self.altitude_change = 0
        self.travel_distance = 0
        self.degrees_traveled = 0

    def _calculate_roll(self, roll_input):
        """
        Calculates the roll changes
        :return:
        """
        self.roll_change = roll_input
        heading_multiplier = self.plane.pitch_roll_to_heading_mods[roll_input]
        self.heading_change += roll_input * heading_multiplier
        return

    def _calculate_pitch(self, pitch_input):
        """
        Calculates the pitch changes
        :return:
        """

        return

    def _calculate_yaw(self, yaw_input):
        """
        Calculates the yaw changes
        :return:
        """

        return

    def _calculate_geeforces(self):
        """
        Calculates the geeforces
        :return:
        """

        return

    def calculate_maneuver(self):
        """
        Calculates the end result of a manuver
        :return:
        """
        # Order is important
        self.heading_change += self.plane.roll_to_heading[self.plane.roll]  # Calculates drift
        self._calculate_roll()
        self._calculate_pitch()
        self._calculate_yaw()
        self._calculate_geeforces()
        return