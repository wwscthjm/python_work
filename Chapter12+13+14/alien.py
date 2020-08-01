import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Behaviors of an alien"""

    def __init__(self, ai_settings, screen):
        """Initialize alien and set its initial location"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load alien's image and obtain outer rectangle
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Each alien should appear at left top corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store location of the alien
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        """Draw alien at given location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Move aliens to the left or right"""
        self.x += self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """"Return True if alien is at screen edge"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left < 0:
            return True