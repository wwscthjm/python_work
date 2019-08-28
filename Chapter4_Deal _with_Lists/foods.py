"""Copy list"""

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]                          #use slicing to traverse

my_foods.append('cannoli')
friend_foods.append('ice cream')

#print('My favorite foods are ')
#print(my_foods)

#print("\nMy friend's favorite foods are ")
#print(friend_foods)

print('My favorite foods are ')
for my_food in my_foods:
    print(my_food)

print("\nMy friend's favorite foods are ")
for friend_food in friend_foods:
    print(friend_food)