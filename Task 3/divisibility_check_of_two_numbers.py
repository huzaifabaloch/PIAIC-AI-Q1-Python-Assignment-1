
class Divisiblity():
	"""
	A model to check if one number is completely divisible by another
	number.
	"""
	
	def __init__(self, numerator, denominator, flag=False):
		"""To initialize the model attributes."""
		self.numerator = numerator
		self.denominator = denominator
		self.flag = flag
		
	def check_divisibility(self):
		"""Check if numerator is completely divisible by denominator."""
		if self.numerator % self.denominator == 0:
			self.flag = True
			
	def display_divisiblity_result(self):
		"""
		Checking flag value, if True or False then returning the result
		well formatted.
		"""
		if self.flag:
			final_result = "Number {} is completely divisible by {}".format(
			self.numerator, self.denominator)
			return final_result
		else:
			final_result = "Number {} is not completely divisible by {}".format(
			self.numerator, self.denominator)
			return final_result
	
	
# START Function.
def run_main():
	
	while True:
		numerator = input("Enter numerator: ")
		if type(numerator) == str and numerator.isdigit():
			denominator = input("Enter denominator: ")
			if type(denominator) == str and denominator.isdigit():
				# Creating an instance of Divisibility.
				div_1 = Divisiblity(int(numerator), int(denominator))
				div_1.check_divisibility()
				print(div_1.display_divisiblity_result())
			else:
				print("Denominator_Error - No strings allowed")
		else:
			print("Numerator_Error - No strings allowed.")
		
		print("\n")
	
# START		
run_main()
