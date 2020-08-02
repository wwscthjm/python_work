"""Create Pygame Window to Respond Users Input"""

import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf


def run_game():
    # Initialize pygame, settings and screen elements
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Create a PLAY button
    play_button = Button(ai_settings, screen, "Play")

    # Create a case to store game stats info and a score board
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Create a ship, a Group of bullets and a Group of aliens
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Create alien fleet
    gf.create_fleet(ai_settings, screen, aliens, ship, stats, bullets)

    # Start game main loop
    while True:
        gf.check_events(ai_settings, screen, ship, aliens, bullets, stats, play_button, sb)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, stats, sb, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()
