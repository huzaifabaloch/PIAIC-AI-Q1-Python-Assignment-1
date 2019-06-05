
def check_number():
	"""Check to see if number is +ve, -ve or zero."""
	
	while True:
		user_number = input("Enter Number: ")
		if user_number == '':
			continue
		
		# removing minus sign from user input and then checking if it
		# is not a digit.
		elif type(user_number) == str and not user_number.lstrip('-').isdigit():
			print("No strings allowed!")
		
		else:
			if int(user_number) < 0:
				print("Negative Number Entered")
			elif int(user_number) > 0:
				print("Positive Number Entered")
			else:
				print("Zero Entered")
			
			continue_checking = input("Continue (y/n) ")
			if continue_checking == 'n':
				break
	
check_number()
