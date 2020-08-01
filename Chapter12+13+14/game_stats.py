import json

class GameStats():
    """Trace statistic info of game"""

    def __init__(self, ai_settings):
        """Initialize statistic info"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # Inactive when game starts
        self.game_active = False
        self.new_fleet = False

        # Do not reset highest score at any time
        self.high_score = self.load_highest_score()

    def reset_stats(self):
        """
        Initialize statistic info which may change while the game goes
        """
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    def load_highest_score(self):
        filename = 'highest_score.json'
        try:
            with open(filename) as f_obj:
                highest_score = json.load(f_obj)
        except FileNotFoundError:
            return 0
        else:
            return highest_score