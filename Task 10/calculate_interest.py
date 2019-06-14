
class InterestCalculator():
	"""
	To model a calculater that can calculate the following:
	A. Simple Interest
	B. Compound Interest
	
	# Using the following:
	1. Principle Amount or Starting Amount
	2. Rate of Interest
	3. Time(in year) or Annum
	
	# Simple Interest
	-> Interest Amount = Principle Amount * Rate * Time
	-> Future Amount = Principle Amount + Interest Amount
	
	# Compound Interest
	-> Interest Amount = Principle Amount * (1 + Rate) ** Time
	-> Future Amount = Interest Amount - Principle Amount
	"""
	
	def __init__(self, principle_amount, interest_rate, year_s=1):
		"""To initialize the attributes of Simple Interest."""
		self.principle_amount = principle_amount
		self.interest_rate = interest_rate
		self.year_s = year_s
		
	def calculate_simple_interest_amount(self):
		"""To calculate the simple interest amount."""
		return (self.principle_amount * self.interest_rate * \
		self.year_s) / 100
		
	def calculate_simple_future_amount(self):
		"""To calculate the future amount of simple interest."""
		interest_amount = self.calculate_simple_interest_amount()
		future_amount = self.principle_amount + interest_amount
		return future_amount
	
	def calculate_compound_interest_amount(self):
		"""To calculate the compound interest amount."""
		return self.principle_amount * ( 1 + self.interest_rate/100) \
		** self.year_s
		
	def calculate_compound_future_amount(self):
		"""To calculate the future amount of compound interest."""
		interest_amount = self.calculate_compound_interest_amount
		future_amount = interest_amount - self.principle_amount
		return future_amount


# Creating an instance of SimpleInterest.
future = InterestCalculator(10000,10,5)
print(future.calculate_simple_future_amount())
