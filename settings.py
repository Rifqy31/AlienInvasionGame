class Settings:
    """A Class to store all settings for Alien Invasion."""
    
    def __init__(self):
        """Initialize the game's static settings."""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (3, 10, 50)

        #ship settings
        self.ship_speed = 1.0
        self.ship_limit = 3

        #bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (8, 230, 0)
        self.bullet_allowed = 3

        #alien settings.
        self.alien_speed = 0.5
        self.fleet_drop_speed = 5
        #Fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = -1

        #Initialized the game speed.
        self.speedup_scale = 1.1
        #How quickly the alien point values increase
        self.score_scale = 1.5


        self.Initialize_dynamic_settings()

    def Initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        self.fleet_direction = -1

        #Scoring
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)