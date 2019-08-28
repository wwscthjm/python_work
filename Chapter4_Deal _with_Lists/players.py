"""Slicing-切片"""

players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three players on my team:")
for player in players[:3]:                              #traverse slicing
    print(player.title())

print("Here are the last three players on my team:")
for player in players[-3:]:
    print(player.title())
