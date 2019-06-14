
def digits_sum_of_a_number(number):
	"""To add digits together of a number."""
	
	# To keep on adding digits of a number.
	digit_add_counter = 0
	
	# Storing digits of a number that will be used for formatting in final
	# output.
	digits_list = []
	
	# For iteration while formatting
	counter = 0
	for each_digit in str(number):
		digits_list.append(each_digit)
		digit_add_counter += int(each_digit)
	
	# Total number of digits.
	length_digits = len(digits_list)
	formatted = ""
	
	# While digits length is not zero.
	while length_digits:
		"""
		formatting each digit of a number. until length_digits is not 
		0 or false, the loop will continue to run and each time, it is 
		taking an item from the digits list and adding in {} brace with 
		+ sign and it keep on adding till the length of digits of number.
		"""
		# rigth striping '+' if it is the last item in the list.
		if length_digits == 1:
			formatted += "{} +".format(digits_list[counter])
			formatted = formatted.rstrip('+')
		else:
			formatted += "{} + ".format(digits_list[counter])
		length_digits -= 1
		counter += 1
		
	
	print("The sum of " + formatted + " is {}".format(digit_add_counter))
		

digits_sum_of_a_number(29223923090739)
