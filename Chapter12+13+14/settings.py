class Settings():
    """Class stores all settings of <Alien Invasion>"""

    def __init__(self):
        """Initialize all game settings"""
        # Screen Setting
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship Setting
        self.ship_speed_factor = 1.5

        # Bullet Setting
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
