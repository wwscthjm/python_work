"""Sort the list"""

cars = ['bmw', 'auid', 'toyato', 'subaru']
#cars.sort()                                         #method "sort()" means stable sort *IN PLACE*
#cars.sort(reverse = True)                           #flag "reverse = True" means stable sort reversely *IN PLACE*
    
#print("Here is the original list:")
#print(cars)
    
#print("\nHere is the sorted list:")
#print(sorted(cars,reverse = True))                  #function "sorted(iterable)" means return a new list containing all items from the iterable in ascending order, and a custom key function can be supplied to customize the sort order, and the reverse flag can be set to request the result in descending order
    
#print("\nHere is the original list again:")
print(cars)

cars.reverse()                                      #method "reverse()" means reverse *IN PLACE*
print(cars)
length = len(cars)                                  #function "len(obj)" means return the number of items in a container
print(length)
