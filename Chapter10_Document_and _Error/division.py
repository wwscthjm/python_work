"""Deal with Errores(ZeroDivisionError and ValueError)"""

#try:
#    print(5/0)
#except ZeroDivisionError:
#    print("You can't divide by zero!")

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
	first_number = input("\nFirst number: ")
	if first_number == 'q':
		break
	second_number = input("Second number: ")
	if second_number == 'q':
		break
	try:
		answer = int(first_number) / int(second_number)
	except ZeroDivisionError:
		print("You can't divide by zero!")
	except ValueError:
		# Deal with Float and String
		try:
			answer = float(first_number) / float(second_number)
		except ZeroDivisionError:
			print("You can't divide by zero!")
		except ValueError:
			# Deal with String
			print("You can't divide strings!")
		else:
			print(answer)
	else:
		print(answer)
