age = 63

if age < 4:
    #print('Your admission cost is $0.')
    price = 0
elif age < 18:
    #print('Your admission cost is $5.')
    price = 5
elif age < 65:
    #print('Your admission cost is $10.')
    price = 10
else:
    #print('Your admission cost is $5.')
    price = 5

print('Your admission cost is $' + str(price) + '.')