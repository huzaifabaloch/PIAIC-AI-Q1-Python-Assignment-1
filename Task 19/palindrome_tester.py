# PALINDROME TESTER.

"""
Lets say we have a word 'civic' which is a palindrome, it means that 
word is same if i read it from beginning or from end, it has exactly the 
same meaning. Now we need someone in the middle of the word that can 
track. lets say the midpoint of civic is 'v'. Now first we will iterate
from begining and storing each character in a first list until we 
encounter the 'v', then we will do the same iteration from end and store
those letters in a second list until we encounter 'v' and break the
loop. And finally we test both the lists, if both have same elements.
then the word is a palindrome, otherwise not palindrome.
"""

def get_word():
	"""To get a word from user."""
	
	user_word = input("Enter a word: ")
	while user_word.isdigit():
		user_word = input("Please enter a word: ")
	
	return user_word


def word_midpoint(user_word):
	"""To get the length of word and the mid-word of a word."""
	
	word_length = len(user_word) 		# Length of word.
	mid_point = word_length / 2  		# Mid-Point of word.
	mid_letter = user_word[int(mid_point)]	# Middle letter that will track.
	
	return word_length, mid_letter
	

def palindrome_tester(word_length, mid_letter, user_word):
	"""for testing a word is palindrome or not."""
	
	# To store letters when iterating from start.
	beginning_test_list = [] 
	
	# To store letters when iterating from end.
	ending_test_list = []
	
	# For indexing.
	counter = 0
	
	while True:
		if user_word[counter] != mid_letter:
			beginning_test_list.append(user_word[counter])
			counter += 1
		
		else:
			counter = word_length - 1 
			while True:
				if user_word[counter] != mid_letter:
					ending_test_list.append(user_word[counter])
					counter -= 1
				else:
					break
			break
	
	return beginning_test_list, ending_test_list
	

def main():
	# START
	
	user_word = get_word()
	word_length, mid_letter = word_midpoint(user_word)
	beginning_test_list, ending_test_list = \
				palindrome_tester(word_length, mid_letter, user_word)
				
	if beginning_test_list == ending_test_list:
		print("\nWord {} is Palindrome.".format(user_word))
	else:
		print("\nWord {} is not Palindrome.".format(user_word))

main()
