"""Simple dictionary"""
"""Nested function"""

#alien_0 = {'color': 'green', 'points': 5}
#print(alien_0)

#print(alien_0['color'])
#print(alien_0['points'])

#new_points = alien_0['points']
#print('You just earned ' + str(new_points) + ' points!')


#alien_0['x_position'] = 0
#alien_0['y_position'] = 25                              #add key-value pair
#print(alien_0)

#alien_0 = {'color': 'green'}
#print("The alien is " + alien_0['color'] + '.')

#alien_0['color'] = 'yellow'                             #change value in the dictionary
#print("The alien is now " + alien_0['color'] + '.')

#del alien_0['points']                                   #delete key-value pair
#print(alien_0)

#alien_0 = {'color': 'green', 'points': '5'}
#alien_1 = {'color': 'yellow', 'points': '10'}
#alien_2 = {'color': 'red', 'points': '15'}

#aliens = [alien_0, alien_1, alien_2]

#for alien in aliens:
#    print(alien)

aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': '5', 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = '10'

for alien in aliens[:5]:
    print(alien)
print("...")

print("Total number of aliens: " + str(len(aliens)))