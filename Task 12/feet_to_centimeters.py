
def feet_to_centimeter(height_in_feet):
	"""
	To convert height in feet to centimeters
	Since --- 1ft = 30.48cm ---
	"""	
	return height_in_feet * 30.48

def main():
	
	height = 0
	print("-- Negative number to exit --\n")
	while height >= 0:
		height_in_feet = float(input("Enter Height in Feet: "))
		if height_in_feet < 0:
			break
		
		height_in_centimeter = feet_to_centimeter(height_in_feet)
		print("\nThere are {}cm in {}ft".format(height_in_centimeter, \
		height_in_feet))
		print('\n')
		
main()
