"""Tuple-元组"""

dimensions = (200, 50)                      #object in a tuple is immutable
print('Original dimensions:')
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)                     #but a tuple is variable
print('\nModified dimension:')
for dimension in dimensions:
    print(dimension)
