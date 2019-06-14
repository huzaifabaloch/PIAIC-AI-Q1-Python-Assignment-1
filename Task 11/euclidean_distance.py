import math

class Euclidean():
	"""
	To model euclidean that can calculate the distance between two 
	points (x1,y1) and (x2,y2)
	"""
	
	def __init__(self, x1, y1, x2, y2):
		"""
		To initialize the points of euclidean to calculate distance
		between two points.
		"""
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2
		
	def calculate_distance_between_two_points(self):
		"""To calculate the distance."""
		distance = math.pow(self.x1 - self.y1, 2) + \
		math.pow(self.x2 - self.y2, 2)
		return math.sqrt(distance)
		
		
def main():
	
	while True:
		x1 = float(input("Enter Co-ordinate for x1: "))
		x2 = float(input("Enter Co-ordinate for x2: "))
		y1 = float(input("Enter Co-ordinate for y1: "))
		y2 = float(input("Enter Co-ordinate for y2: "))
		# Creating an instance of Euclidean.
		eucli = Euclidean(x1, y1, x2, y2)
		distance = eucli.calculate_distance_between_two_points()
		formatted_answer = "\nDistance between points ({},{}) and".format(
		x1,x2) + " ({},{}) is {}\n".format(y1,y2,distance)
		print(formatted_answer)
		user_continue = input("Continue using ? (y/n) ")
		if user_continue == 'n':
			break
		print('\n')

main()
