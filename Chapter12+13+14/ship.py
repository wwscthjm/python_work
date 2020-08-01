import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """Behaviors of ships"""

    def __init__(self, ai_settings, screen):
        """Initialize ship and set initial position"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load ship's image and obtain outer rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Put ship ship at the bottom centre of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store fiction values in ship property
        self.center = [float(self.rect.centerx), float(self.rect.bottom)]

        # Moving sign
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

    def update(self):
        """Move ship according to moving signs"""
        # Update center, not rect
        if self.moving_up and self.rect.top > 0:
            self.center[1] -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center[1] += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center[0] -= self.ai_settings.ship_speed_factor
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center[0] += self.ai_settings.ship_speed_factor

        # Update rect according to self.center
        self.rect.centerx = self.center[0]
        self.rect.bottom = self.center[1]

    def blitme(self):
        """Print ship at the given position"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Hold back ship to its original location"""
        self.center = [float(self.screen_rect.centerx), float(self.screen_rect.bottom)]

    def hold_back_ship(self):
        """Make sure the ship does not hit the new fleet"""
        self.center[1] = self.screen.get_rect().bottom
        self.blitme()
