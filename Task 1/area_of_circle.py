import math

class Circle():
	"""To model a circle that can calculate area of circle."""
	
	def __init__(self, radius):
		"""
		To initialize the attribute that will calculate area of
		circle
		"""
		self.radius = radius
		
	def calculate_area_of_circle(self):
		"""To calculate the area of cirlce."""
		return round((math.pi * (self.radius ** 2)), 7)
				
	def display_formatted_area_of_circle(self):
		"""To return area of circle formatted."""
		area_of_circle = self.calculate_area_of_circle()
		formated_result = "Area of Circle with radius {} is {}".format(
						  self.radius, area_of_circle)
		return formated_result
		
		
def run_program():
	
	while True:
		user_input = input("Input Radius: ")
		if type(user_input) == str:
			if '.' not in user_input and not user_input.isdigit():
				print("Sorry no strings allowed!")
			
			# replace the dot with empty string that occuring one time,
			# and then checking if a string is not containing digit.
			elif not user_input.replace('.','',1).isdigit(): 
				print("Sorry no strings allowed!")
				
			else:
				# Creating an instance of Circle()
				circle_1 = Circle(float(user_input))
				print(circle_1.display_formatted_area_of_circle())
				program_continue = input("Continue (y/n) ")
				if program_continue == 'n':
					break
				print("\n")
# START 		
run_program()
			
			
			


	
