"""Isolate Functions with Main File"""

import sys
import pygame
from time import sleep
import json

from bullet import Bullet
from alien import Alien

def save_highest_score(stats):
	"""Save the highest score"""
	filename = 'highest_score.json'
	with open(filename, 'w') as f_obj:
		json.dump(stats.high_score, f_obj)

def check_keydown_events(event, ai_settings, stats, sb, screen, ship, bullets, aliens):
	"""Respond to PRESS"""
	if event.key == pygame.K_UP:
		ship.moving_up = True
	elif event.key == pygame.K_DOWN:
		ship.moving_down = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_SPACE and not stats.new_fleet:
		fire_bullets(ai_settings, screen, ship, bullets)
	elif event.key == pygame.K_q:
		save_highest_score(stats)
		sys.exit()
	elif event.key == pygame.K_p and not stats.game_active:
		start_game(ai_settings, aliens, bullets, screen, ship, stats, sb)

def fire_bullets(ai_settings, screen, ship, bullets):
	"""If not reach the limit, fire a bullet"""
	if len(bullets) < ai_settings.bullet_allowed:
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

def start_game(ai_settings, aliens, bullets, screen, ship, stats, sb):
	"""Start game"""
	# Reset dynamic settings
	ai_settings.initialize_dynamic_settings()

	pygame.mouse.set_visible(False)
	
	# Reset game stats info
	stats.reset_stats()
	stats.game_active = True
	sb.prep_images()
	sb.show_score()
	
	# Clear all aliens and bullets
	aliens.empty()
	bullets.empty()
	
	# Create a new fleet of aliens and place ship at its original location
	create_fleet(ai_settings, screen, aliens, ship, stats, bullets)
	ship.center_ship()

def check_play_button(ai_settings, screen, play_button, stats, sb, mouse_x, mouse_y, ship, aliens, bullets):
	"""Start game when user click Play button"""
	button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
	if button_clicked and not stats.game_active:
		start_game(ai_settings, aliens, bullets, screen, ship, stats, sb)

def check_events(ai_settings, screen, ship, aliens, bullets, stats, play_button, sb):
	"""Respond keyboard and mouse events"""
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				save_highest_score(stats)
				sys.exit()

			elif event.type == pygame.KEYDOWN:
				# Check value of event.key
				#print(event.key)
				check_keydown_events(event, ai_settings, stats, sb, screen, ship, bullets, aliens)

			elif event.type == pygame.KEYUP:
				check_keyup_events(event, ship)

			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_x, mouse_y = pygame.mouse.get_pos()
				check_play_button(ai_settings, screen, play_button, stats, sb, mouse_x, mouse_y, ship, aliens, bullets)

def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
	"""Update images on screen, and switch to new screen"""
	# Re-draw screen at every loops
	screen.fill(ai_settings.bg_color)
	if stats.game_active:
		for bullet in bullets.sprites():
			bullet.draw_bullet()
	ship.blitme()
	aliens.draw(screen)

	# Show the score
	sb.show_score()

	# Draw play button if game is inactive
	if not stats.game_active:
		play_button.draw_button()

	# Make the last screen-drawing visable
	pygame.display.flip()

def start_new_level(sb, stats):
	"""Increase level"""
	stats.level += 1
	sb.prep_level()

def check_bullet_alien_collisions(ai_settings, stats, sb, aliens, bullets, screen, ship):
	"""Respond to collisions between aliens and bullets"""
	# Check if there's any bullet hitting any alien
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

	if collisions:
		for aliens in collisions.values():
			stats.score += ai_settings.alien_points * len(aliens)
			sb.prep_score()
		check_high_score(stats, sb)

	if len(aliens) == 0:
		# Delete all existing bullets , speed up the game and create a new alien fleet
		bullets.empty()
		ship.hold_back_ship()
		ship.blitme()
		ai_settings.increase_speed()

		# Increase level
		start_new_level(sb, stats)

		create_fleet(ai_settings, screen, aliens, ship, stats, bullets)

def update_bullets(ai_settings, stats, sb, screen, ship, aliens, bullets):
	"""Update bullets' locations and delete disappeared bullets"""
	# Update bullets' locations
	if stats.new_fleet:
		bullets.empty()
		stats.new_fleet = False
	bullets.update()

	# Delete disappeared bullets
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

	check_bullet_alien_collisions(ai_settings, stats, sb, aliens, bullets, screen, ship)

def create_fleet(ai_settings, screen, aliens, ship, stats, bullets):
	"""Create alien fleet"""
	# Create an alien and calculate number of aliens which a row can contain
	# Space between aliens is width of alien
	bullets.empty()
	stats.new_fleet = True
	alien = Alien(ai_settings, screen)
	number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
	number_rows = get_number_aliens_rows(ai_settings, ship.rect.height, alien.rect.height)

	# Create a row of aliens
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(ai_settings, screen, aliens, alien_number, ship, row_number)
		
def get_number_aliens_x(ai_settings, alien_width):
	"""Calculate nunber of aliens in one row"""
	available_space_x = ai_settings.screen_width - 2 * alien_width
	number_aliens_x = int(available_space_x / (2 * alien_width))
	return number_aliens_x

def get_number_aliens_rows(ai_settings, ship_height, alien_height):
	"""Calculate nunber of rows in all available space"""
	available_space_y = ai_settings.screen_height - 4 * alien_height - ship_height
	number_rows = int(available_space_y / (4 * alien_height))
	return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, ship, row_number):
	# Create an alien and add it into current row
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 4 * alien.rect.height * row_number
	aliens.add(alien)

	# Create an alien and add it into next row
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	alien.rect.y = 3 * alien.rect.height + 4 * alien.rect.height * row_number
	alien.x = ship.screen_rect.right - 2 * alien_width * (alien_number + 1) - alien_width
	alien.rect.x = alien.x
	aliens.add(alien)

def ship_hit(ai_settings, aliens, bullets, screen, ship, stats, sb):
	"""Respond to the ship hit by aliens"""
	if stats.ships_left > 0:
	    # Ship's lives minus 1
		if not stats.new_fleet:
			stats.ships_left -= 1

		# Update score board
		sb.prep_ships()
		
		# Clear all aliens and bullets
		bullets.empty()
		aliens.empty()
		
		
		# Create a new fleet of aliens and place ship at its original location
		create_fleet(ai_settings, screen, aliens, ship, stats, bullets)
		ship.center_ship()
		
		# Pulse
		sleep(0.5)

	else:
		stats.game_active = False
		pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings, aliens, bullets, screen, ship, stats, sb):
	"""Check if there is any alien reaching the screen bottom"""
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			# Respond like hitting a ship
			ship_hit(ai_settings, aliens, bullets, screen, ship, stats, sb)
			break

def update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets):
	"""
	Check if any aliens moving to the edge and 
	update all each location of aliens fleet
	"""
	check_fleet_edges(ai_settings, aliens)
	aliens.update()

	# Check the collision between aliens and ship
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(ai_settings, aliens, bullets, screen, ship, stats, sb)

	# Check if there is any alien reaching the screen bottom
	check_aliens_bottom(ai_settings, aliens, bullets, screen, ship, stats, sb)

def check_fleet_edges(ai_settings, aliens):
	"""Take corresponding messure if alien reaches edge"""
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings, aliens)
			break

def change_fleet_direction(ai_settings, aliens):
	"""Moving down the fleet, and change its direction"""
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1

def check_high_score(stats, sb):
	"""Check if it is a new highest score"""
	if stats.score > stats.high_score:
		stats.high_score = stats.score
		sb.prep_high_score()
