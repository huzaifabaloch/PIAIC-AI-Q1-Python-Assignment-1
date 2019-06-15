
def get_text():
	"""Get a text from user."""
	user_text = input("Enter text: ")
	return user_text

def count_vowels_and_consonants(user_text):
	"""Count vowels and consonants from user text."""
	vowels_counter = 0
	consonants_counter = 0
	
	# Iterate each letter in the text annd checking if a letter occurs
	# in the list of vowels. 
	for each_letter in user_text:
		if each_letter in ['a', 'e', 'i', 'o', 'u']:
			vowels_counter += 1
		elif each_letter == ' ':
			continue 
		else:
			consonants_counter += 1
	
	return vowels_counter, consonants_counter	

def main():
	user_text = get_text()
	vowels_counter, consonants_counter = \
								count_vowels_and_consonants(user_text)
	print("Vowels : {}\nConsonants : {}".format(vowels_counter,\
												consonants_counter))

main()
