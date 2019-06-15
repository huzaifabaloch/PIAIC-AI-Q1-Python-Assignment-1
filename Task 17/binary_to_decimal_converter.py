

def get_binary_number():
	binary_number = input("Enter a Binary number: ")
	while not binary_number.isdigit():
		binary_number = input("Enter a Binary number: ")
	return binary_number
	

def convert_binary_to_decimal(binary_number):
	return int(binary_number, 2)


def main():
	binary_number = get_binary_number()
	decimal_number = convert_binary_to_decimal(binary_number)
	print("Decimal Representation of {} is {}".format(binary_number,\
	decimal_number))


main()

