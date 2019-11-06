"""Simple dictionary"""

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

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

del alien_0['points']                                   #delete key-value pair
print(alien_0)