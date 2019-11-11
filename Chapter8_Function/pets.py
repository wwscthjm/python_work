"""Positional Arguements"""
"""Key-word Arguements"""

def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的信息"""
    print("I have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".\n")

#describe_pet('hamster', 'harry')
#describe_pet('dog', 'willie')

describe_pet(pet_name='harry', animal_type='hamster')
describe_pet('willie')