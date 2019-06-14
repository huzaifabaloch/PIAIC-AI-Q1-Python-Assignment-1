import math

class Sphere():
	""""To model the sphere that can calulate it's volume."""
	
	def __init__(self, radius):
		"""To initialize the class attributes."""
		self.radius = radius
		
	def calculate_volume_of_sphere(self):
		"""
		Calculate the volume of a sphere where the formula is:
		volume = 4/3 * pi * r^3.
		"""
		return 4/3 * math.pi * self.radius ** 3
		
	def show_calculated_volume_of_sphere(self):
		"""To display the calculated result of volume of sphere."""
		volume = self.calculate_volume_of_sphere()
		formatted_output = "The volume of Sphere with Radius {} is {}".format(
		self.radius, round(volume, 3))
		print(formatted_output)
	
		
def run_program():
	# START
	
	user_radius = 0
	while user_radius >= 0:
		user_radius = int(input("Enter Radius of Sphere: "))
		if user_radius < 0:
			break
			
		# Creating an instance of Sphere
		sphere_1 = Sphere(user_radius)
		sphere_1.show_calculated_volume_of_sphere()


# Run Program		
run_program()		
		
		
