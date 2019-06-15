# Count Alphabets, Numbers and Special Characters.

def list_of_alphabets():
	"""Returns list of alphabets."""
	
	alphabets = []
	for i in range(65, 91):
		alphabets.append(chr(i))
	for i in range(97, 123):
		alphabets.append(chr(i))
	
	return alphabets
	
def list_of_digits():
	"""Returns list of digits."""
	
	digits = []
	for i in range(48, 58):
		digits.append(chr(i))
		
	return digits

def get_text():
	"""Returns user text."""
	
	user_text = input("Enter text: ")
	return user_text
	
def text_counter(user_text):
	"""
	To count alphabets, digits, special characters and spaces from
	user text.
	"""
	
	alphabets_counter = 0
	digits_counter = 0
	special_characters_counter = 0
	spaces_counter = 0
	
	for each in user_text:
		if each in list_of_alphabets():
			alphabets_counter += 1
		elif each in list_of_digits():
			digits_counter += 1
		elif each == " ":
			spaces_counter += 1
		else:
			special_characters_counter += 1
			
	return alphabets_counter, digits_counter, \
	special_characters_counter, spaces_counter
	
def main():
	# START
	
	user_text = get_text()
	text_counter(user_text)
	alphabets_counter, digits_counter, special_characters_counter, \
	spaces_counter = text_counter(user_text)
	
	print("\n")
	print("Numbers = {}".format(digits_counter))
	print("Alphabets = {}".format(alphabets_counter))
	print("Special Characeters = {}".format(special_characters_counter))
	print("Spaces = {}".format(spaces_counter))

main()
