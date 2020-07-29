import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Behaviors of bullets"""

    def __init__(self, ai_settings, screen, ship):
        """Create a bullet element at the ship's location"""
        super().__init__()
        self.screen = screen

        # Create a rectangle to represent a bullet, and locate it at correct location
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store fiction values of location
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Move bullets to the top"""
        # Update fiction value of location
        self.y -= self.speed_factor
        # Update rect location of bullet
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw bullets on screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)