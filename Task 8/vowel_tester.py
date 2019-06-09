
def vowel_tester(letter):
	"""To test a vowel a,e,i,o,u on user input."""
	
	if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u' or letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U':
		print("letter '{}' is vowel.".format(letter))
	else:
		print("letter '{}' is not vowel.".format(letter))

def run_program():
	"""START"""
	print("Number to exit.\n")
	
	while True:
		character = input("Enter a character: ")
		if len(character) != 1:
			print("Please enter one character.\n")
			continue
		if not character.isdigit():
			vowel_tester(character)
		else:
			break
		print("\n")
		
run_program()
