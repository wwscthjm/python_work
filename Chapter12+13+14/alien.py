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
