class StandardPlane:

    def __init__(self, name):
        self.name = name

        self.pitch = 0
        self.roll = 0
        self.yaw = 0
        self.airspeed = 0
        self.altitude = 0

        self.roll_pitch_mods = {
            0: {
                "pitch_per_pitch": 1,
                "heading_per_pitch": 0
            },
            15: {
                "pitch_per_pitch": 1,
                "heading_per_pitch": 0.25
            },
            30: {
                "pitch_per_pitch": .5,
                "heading_per_pitch": 0.33334
            },
            45: {
                "pitch_per_pitch": .5,
                "heading_per_pitch": 0.5
            },
            60: {
                "pitch_per_pitch": .33334,
                "heading_per_pitch": 0.5
            },
            75: {
                "pitch_per_pitch": .25,
                "heading_per_pitch": 1
            },
            90: {
                "pitch_per_pitch": 0,
                "heading_per_pitch": 1
            },
            105: {
                "pitch_per_pitch": -.25,
                "heading_per_pitch": 1
            },
            120: {
                "pitch_per_pitch": -.33334,
                "heading_per_pitch": 0.5
            },
            135: {
                "pitch_per_pitch": -.5,
                "heading_per_pitch": 0.5
            },
            150: {
                "pitch_per_pitch": -.5,
                "heading_per_pitch": 0.33334
            },
            165: {
                "pitch_per_pitch": -1,
                "heading_per_pitch": 0.25
            },
            180: {
                "pitch_per_pitch": -1,
                "heading_per_pitch": 0
            },
            -15: {
                "pitch_per_pitch": 1,
                "heading_per_pitch": -0.25
            },
            -30: {
                "pitch_per_pitch": .5,
                "heading_per_pitch": -0.33334
            },
            -45: {
                "pitch_per_pitch": .5,
                "heading_per_pitch": -0.5
            },
            -60: {
                "pitch_per_pitch": .33334,
                "heading_per_pitch": -0.5
            },
            -75: {
                "pitch_per_pitch": .33334,
                "heading_per_pitch": -0.5
            },
            -90: {
                "pitch_per_pitch": 0,
                "heading_per_pitch": -1
            },
            -105: {
                "pitch_per_pitch": -.25,
                "heading_per_pitch": -1
            },
            -120: {
                "pitch_per_pitch": -.33334,
                "heading_per_pitch": -0.5
            },
            -135: {
                "pitch_per_pitch": -.5,
                "heading_per_pitch": -0.5
            },
            -150: {
                "pitch_per_pitch": -.5,
                "heading_per_pitch": -0.33334
            },
            -165: {
                "pitch_per_pitch": -1,
                "heading_per_pitch": -0.25
            }
        }
        self.roll_yaw_mods = {
            0: {
                "heading_per_yaw": 1,
                "pitch_per_yaw": 0
            },
            15: {
                "heading_per_yaw": 1,
                "pitch_per_yaw": 0.25
            },
            30: {
                "heading_per_yaw": .5,
                "pitch_per_yaw": 0.33334
            },
            45: {
                "heading_per_yaw": .5,
                "pitch_per_yaw": 0.5
            },
            60: {
                "heading_per_yaw": .33334,
                "pitch_per_yaw": 0.5
            },
            75: {
                "heading_per_yaw": .25,
                "pitch_per_yaw": 1
            },
            90: {
                "heading_per_yaw": 0,
                "pitch_per_yaw": 1
            },
            105: {
                "heading_per_yaw": -.25,
                "pitch_per_yaw": 1
            },
            120: {
                "heading_per_yaw": -.33334,
                "pitch_per_yaw": 0.5
            },
            135: {
                "heading_per_yaw": -.5,
                "pitch_per_yaw": 0.5
            },
            150: {
                "heading_per_yaw": -.5,
                "pitch_per_yaw": 0.33334
            },
            165: {
                "heading_per_yaw": -1,
                "pitch_per_yaw": 0.25
            },
            180: {
                "heading_per_yaw": -1,
                "pitch_per_yaw": 0
            },
            -15: {
                "heading_per_yaw": 1,
                "pitch_per_yaw": -0.25
            },
            -30: {
                "heading_per_yaw": .5,
                "pitch_per_yaw": -0.33334
            },
            -45: {
                "heading_per_yaw": .5,
                "pitch_per_yaw": -0.5
            },
            -60: {
                "heading_per_yaw": .33334,
                "pitch_per_yaw": -0.5
            },
            -75: {
                "heading_per_yaw": .33334,
                "pitch_per_yaw": -0.5
            },
            -90: {
                "heading_per_yaw": 0,
                "pitch_per_yaw": -1
            },
            -105: {
                "heading_per_yaw": -.25,
                "pitch_per_yaw": -1
            },
            -120: {
                "heading_per_yaw": -.33334,
                "pitch_per_yaw": -0.5
            },
            -135: {
                "heading_per_yaw": -.5,
                "pitch_per_yaw": -0.5
            },
            -150: {
                "heading_per_yaw": -.5,
                "pitch_per_yaw": -0.33334
            },
            -165: {
                "heading_per_yaw": -1,
                "pitch_per_yaw": -0.25
            }
        }
        self.roll_to_heading = {
            0: 0,
            15: 5,
            30: 10,
            45: 15,
            60: 20,
            75: 25,
            90: 30,
            105: 25,
            120: 20,
            135: 15,
            150: 10,
            165: 5,
            180: 0,
            -15: -5,
            -30: -10,
            -45: -15,
            -60: -20,
            -75: -20,
            -90: -30,
            -105: -25,
            -120: -20,
            -135: -15,
            -150: -10,
            -165: -5
        }