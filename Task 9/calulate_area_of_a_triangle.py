
class Triangle():
	"""
	To model a Triangle that can calculate the area of triangle:
	Area = Base * Height / 2 or Area = 1/2 * Base * Height
	"""
	
	def __init__(self, base, height):
		"""To initialize the base and height of a triangle."""
		self.base = base
		self.height = height
		
	def calculate_area_of_a_triangle(self):
		"""To calculate the area of a triangle."""
		return (1/2) * self.base * self.height
		
	def show_area_of_a_triangle(self):
		"""To display the calculated area of triangle."""
		area = self.calculate_area_of_a_triangle()
		formatted_answer = "Area of a Triangle with Height {} and Base {} is {}".format(
		self.base, self.height, area)
		print(formatted_answer)
	

def run_program():
	# START
	
	print('-- Enter a letter to exit anytime --\n')
	while True:
		print("\n")
		base = input("Enter magnitude of Triangle base: ")
		if base is '0':
			print("Please input non-zero number.")
			continue
		elif not base.isdigit():
			break	
			
		height = input("Enter magnitude of Triangle height: ")
		if height is '0':
			print("Please input non-zero number.")
			continue
		elif not height.isdigit():
			break	
			
		# Creating an instance of Triangle.
		triangle_1 = Triangle(int(base), int(height))
		triangle_1.show_area_of_a_triangle()	
		
		
		
run_program()

