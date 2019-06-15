
def user_decimal_number():
	decimal_number = input("Enter a decimal number: ")
	while not decimal_number.isdigit():
		decimal_number = input("Enter a decimal number: ")
	return int(decimal_number)

def convert_decimal_to_binary(decimal_number):
	return bin(decimal_number)
	
def split_0b():
	decimal_number = user_decimal_number()
	binary_number = convert_decimal_to_binary(decimal_number)
	binary_number = binary_number.lstrip('0b')
	return decimal_number, binary_number
		
def main():
	decimal_number, binary_number = split_0b()
	print("Binary Representation of {} is {}".format(decimal_number,\
	binary_number))
	
# START
main()
