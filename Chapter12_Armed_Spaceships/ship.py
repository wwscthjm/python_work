import pygame

class Ship():
    """Behaviors of ships"""

    def __init__(self, screen):
        """Initialize ship and set initial position"""
        self.screen = screen

        # Load ship's image and obtain outer rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Put ship ship at the bottom centre of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Print ship at given position"""
        self.screen.blit(self.image, self.rect)
