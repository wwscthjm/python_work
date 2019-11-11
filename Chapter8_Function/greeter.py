"""Define Function"""
"""Combine Function and While Loop"""

#def greet_user(username):
#    """显示简单的问候语"""
#    print("Hello, " + username.title() + "!")

#greet_user('jesse')

def get_formatted_name(first_name, last_name):
    """Return formatted name"""
    full_name = first_name + " " + last_name
    return full_name.title()

while True:
    print("\nPlease tell your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First_name: ")
    if f_name == 'q':
        break

    l_name = input("Last_name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")