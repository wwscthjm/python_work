class Settings():
    """Class stores all settings of <Alien Invasion>"""

    def __init__(self):
        """Initialize all game static settings"""
        # Screen Setting
        self.screen_width = 1250
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship Setting
        self.ship_limit = 3

        # Bullet Setting
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 5

        # Alien Setting
        self.fleet_drop_speed = 10

        # Acceloration of game
        self.speedup_scale = 1.1

        # Accleoration of alien's points
        self.score_scale = 1.5

        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        """Initialize game dynamic settings"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet_direction = 1 means moving right, = -1 meansmoving left
        self.fleet_direction = 1

        # Set score
        self.alien_points = 50

    def increase_speed(self):
        """Speed and alien points increasement settings"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
