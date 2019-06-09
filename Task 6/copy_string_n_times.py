
def string_copy(user_string, no_of_copy):
	"""Copy user string n number of times."""
	
	return user_string * no_of_copy


def run_program():
	# START
	
	no_of_copy = 0
	while no_of_copy >= 0:
		user_input = input("Enter String: ")
		if user_input == '':
			continue
		no_of_copy = int(input("How many copies of String you need: "))
		print(string_copy(user_input, no_of_copy))

# RUN PROGRAM
run_program()
