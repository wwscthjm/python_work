"""Sample of IF statement"""

cars = ['bmw', 'auid', 'toyato', 'subaru']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())