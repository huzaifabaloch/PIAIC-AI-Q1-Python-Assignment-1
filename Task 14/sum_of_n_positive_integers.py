

def sum_of_n_postive_number(n_number):
	"""To sum n postive integers."""
	
	sum_counter = 0
	while n_number != 0:
		sum_counter += n_number
		n_number -= 1
	return sum_counter 
		
def run_program():
	"""START"""
	
	while True:
		n_number = int(input("Enter value of n: "))
		if n_number > 0:
			sum_count = sum_of_n_postive_number(n_number)
			print("Sum of {} Positive integer is {}.".format(n_number, sum_count))
		else:
			break

run_program()
