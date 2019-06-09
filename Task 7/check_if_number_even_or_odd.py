
def even_odd_test(number):
	"""Check whether number is even or odd."""
	
	if number % 2 == 0:
		print("{} is Even.".format(number))
	else:
		print("{} is Odd.".format(number))
		
def run_program():
	
	print("Even | Odd Test\n")
	while True:
		user_number = int(input("Enter a non-negative number: "))
		if user_number < 0:
			break
		
		even_odd_test(user_number)

# START
run_program()
