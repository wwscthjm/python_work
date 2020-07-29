"""Isolate Functions with Main File"""

import sys
import pygame

from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai_settings, screen, ship, bullets):
	"""Respond to PRESS"""
	if event.key == pygame.K_UP:
		ship.moving_up = True
	elif event.key == pygame.K_DOWN:
		ship.moving_down = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_SPACE:
		fire_bullets(ai_settings, screen, ship, bullets)
	elif event.key == pygame.K_q:
		sys.exit()

def fire_bullets(ai_settings, screen, ship, bullets):
	"""Fire a bullet"""
	# Create a bullet, and add it into Group bullects
	new_bullet = Bullet(ai_settings, screen, ship)
	bullets.add(new_bullet)

def check_keyup_events(event, ship):
	"""Respond to RELEASE"""
	if event.key == pygame.K_UP:
		ship.moving_up = False
	elif event.key == pygame.K_DOWN:
		ship.moving_down = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False
	elif event.key == pygame.K_RIGHT:
		ship.moving_right = False

def check_events(ai_settings, screen, ship, bullets):
	"""Respond keyboard and mouse events"""
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			elif event.type == pygame.KEYDOWN:
				# Check value of event.key
				#print(event.key)
				check_keydown_events(event, ai_settings, screen, ship, bullets)

			elif event.type == pygame.KEYUP:
				check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, aliens, bullets):
	"""Update images on screen, and switch to new screen"""
	# Re-draw screen at every loops
	screen.fill(ai_settings.bg_color)
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	aliens.draw(screen)

	# Make the last screen-drawing visable
	pygame.display.flip()

def update_bullets(bullets):
	"""Update bullets' locations and delete disappeared bullets"""
	# Update bullets' locations
	bullets.update()

	# Delete disappeared bullets
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

def create_fleet(ai_settings, screen, aliens):
	"""Create alien fleet"""
	# Create an alien and calculate number of aliens which a row can contain
	# Space between aliens is width of alien
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	available_space_x = ai_settings.screen_width - 2 * alien_width
	number_aliens_x = int(available_space_x / (2 * alien_width))

	# Create a row of aliens
	for alien_number in range(number_aliens_x):
		# Create an alien and add it into current row
		alien = Alien(ai_settings, screen)
		alien.x = alien_width + 2 * alien_width * alien_number
		alien.rect.x = alien.x
		aliens.add(alien)