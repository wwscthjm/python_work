"""Save and Load User's data"""

import json

def get_stored_username():
	"""如果以前存储了用户名，就加载它"""
	filename = 'username.json'
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return username

def get_new_username():
	"""提示用户输入用户名"""
	username = input("What is your name? ")
	filename = 'username.json'
	with open(filename, 'w') as f_obj:
		json.dump(username, f_obj)
	return username

def greet_user():
	"""问候用户，并指出其名字"""
	username = get_stored_username()
	if username:
		name_error = input(f"Hi, is your name {username}? (Y/n)")
		while True:
			if name_error is 'Y':
				print(f"Welcome back, {username}!")
				break
			elif name_error is 'n':
				username = get_new_username()
				print(f"Welcome back, {username}!\nWe'll remember you when you come back next time.")
				break
			else:
				name_error = input("Please re-type: (Y/n)")
	else:
		username = get_new_username()
		print(f"We'll remember you when you come back, {username}!")
		
greet_user()