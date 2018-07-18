#motocycles = ['honda', 'yamaha', 'suzuki']
#print(motocycles)

##motocycles[0] = 'ducati'
##print(motocycles)

#motocycles.append('ducati')
#print(motocycles)

motocycles = []

motocycles.append('honda')
motocycles.append('yamaha')
motocycles.append('suzuki')

#print(motocycles)

#motocycles.insert(0, 'ducati')
#print(motocycles)

#del motocycles[0]                   #The value of motocycles[0] doesn't exist anymore.
#print(motocycles)

#popped_motocycle = motocycles.pop() #The last value of motocycles[0] is popped out and saved in new variable.
#print(motocycles)
#print(popped_motocycle)

#first_owned = motocycles.pop(0)
#print('The first motocycle I owned was a ' + first_owned.title() + '.')

motocycles.insert(-1,'ducati')
print(motocycles)

too_expensive = 'ducati'
motocycles.remove(too_expensive)
print(motocycles)
print("\nA " + too_expensive.title() + " is too expnsive for me.")