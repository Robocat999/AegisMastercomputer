class ValueBasedCalculator:
    """
    Makes predictions based off of plane values
    """

    def __init__(self):
        self.DEGREE_OF_CHANGE_DIVISOR = 15

        self.plane = None
        self.maneuver_airspeed = 0

        self.pitch_change = 0
        self.roll_change = 0
        self.heading_change = 0
        self.airspeed_change = 0
        self.altitude_change = 0
        self.travel_distance = 0
        self.degrees_traveled = 0
        self.degree_of_change_corrections = 0

    def _reset_calculator_values(self):
        """
        Resets the numerical values stored in the calculator. Use before starting a new calculation
        :return:
        """
        self.maneuver_airspeed = 0

        self.pitch_change = 0
        self.roll_change = 0
        self.heading_change = 0
        self.airspeed_change = 0
        self.altitude_change = 0
        self.travel_distance = 0
        self.degrees_traveled = 0
        self.degree_of_change_corrections = 0
        self.geeforces = 0
        return

    def _calculate_roll(self, roll_input):
        """
        Calculates the roll changes
        :return:
        """
        self.roll_change += roll_input
        heading_multiplier = self.plane.pitch_roll_to_heading_mods[self.plane.pitch]
        self.heading_change += roll_input * heading_multiplier
        return

    def _calculate_pitch(self, pitch_input):
        """
        Calculates the pitch changes
        :return:
        """
        current_plane_roll = self.plane.roll + self.roll_change
        pitch_multiplier = self.plane.roll_pitch_mods[current_plane_roll]["pitch_per_pitch"]
        heading_multiplier = self.plane.roll_pitch_mods[current_plane_roll]["heading_per_pitch"]
        self.pitch_change += pitch_input * pitch_multiplier
        self.heading_change += pitch_input * heading_multiplier
        return

    def _calculate_yaw(self, yaw_input):
        """
        Calculates the yaw changes
        :return:
        """
        current_roll = self.plane.roll + self.roll_change
        current_pitch = self.plane.pitch + self.pitch_change

        roll_pitch_modifier = self.plane.roll_yaw_mods[current_roll]["pitch_per_yaw"]
        roll_heading_modifier = self.plane.roll_yaw_mods[current_roll]["heading_per_yaw"]

        pitch_heading_modifier = self.plane.pitch_yaw_mods[current_pitch]["heading_per_yaw"]
        pitch_pitch_modifier = self.plane.pitch_yaw_mods[current_pitch]["pitch_per_yaw"]
        pitch_roll_modifier = self.plane.pitch_yaw_mods[current_pitch]["roll_per_yaw"]

        self.pitch_change += (yaw_input * roll_pitch_modifier) + (yaw_input * pitch_pitch_modifier)
        self.heading_change += (yaw_input * roll_heading_modifier) + (yaw_input + pitch_heading_modifier)
        self.roll_change += yaw_input * pitch_roll_modifier

        if "true_degree_of_change_correction" in self.plane.pitch_yaw_mods[current_pitch]:
            self.degree_of_change_corrections += self.plane.pitch_yaw_mods[current_pitch]["true_degree_of_change_correction"]

        return

    def _calculate_geeforces(self):
        """
        Calculates the geeforces
        :return:
        """
        degree_of_change = self.roll_change + self.pitch_change + self.heading_change + self.degree_of_change_corrections
        self.geeforces = self.plane.velocity * (degree_of_change / self.DEGREE_OF_CHANGE_DIVISOR) * self.plane.stick_pos_modifier
        return

    def calculate_maneuver(self, roll_input, pitch_input, yaw_input):
        """
        Calculates the end result of a manuver
        :return:
        """
        # Order is important
        self._reset_calculator_values()
        self.heading_change += self.plane.roll_to_heading[self.plane.roll]  # Calculates drift
        self._calculate_roll(roll_input)
        self._calculate_pitch(pitch_input)
        self._calculate_yaw(yaw_input)
        self._calculate_geeforces()
        return