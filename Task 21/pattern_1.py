

def get_pattern_size():
	
	pattern_size = int(input("Enter patter's size: "))
	while pattern_size < 0:
		pattern_size = int(input("Enter positive pattern's size: "))
	return pattern_size

def make_pattern(pattern_size):

	counter = pattern_size
	
	for i in range(pattern_size):
		print(i * '*')
	while counter != 0:
		print(counter * '*')
		counter -= 1

def main():
	# START
	
	pattern_size = get_pattern_size()
	make_pattern(pattern_size)
		
main()
	
	
