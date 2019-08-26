"""Change, Add and Delete objects"""

motocycles = ['honda', 'yamaha', 'suzuki']
#print(motocycles)

#motocycles[0] = 'ducati'                       #redefine the first object
#print(motocycles)

#motocycles.append('ducati')                    #method "append()" means append object to the end of the list
#print(motocycles)

motocycles = []

motocycles.append('honda')
motocycles.append('yamaha')
motocycles.append('suzuki')

#print(motocycles)

#motocycles.insert(0, 'ducati')                 #method "insert()" means insert object before index
#print(motocycles)

#del motocycles[0]                              #"del" means delete object
#print(motocycles)

#popped_motocycle = motocycles.pop()            #method "pop()" means remove and return item at index(default last)
#print(motocycles)
#print(popped_motocycle)

#first_owned = motocycles.pop(0)
#print('The first motocycle I owned was a ' + first_owned.title() + '.')

motocycles.insert(-1,'ducati')                  #index "-n" means the last n object
print(motocycles)

too_expensive = 'ducati'
motocycles.remove(too_expensive)                #method "remove()" means remove the first occurrance of value
print(motocycles)
print("\nA " + too_expensive.title() + " is too expnsive for me.")

"""Extra"""
#When deleting object from list, you can use "del" if you do not need this object any more, or use method "pop('index')" on the contrary.
