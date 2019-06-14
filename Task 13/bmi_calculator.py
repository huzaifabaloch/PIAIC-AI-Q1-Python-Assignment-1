
def get_info():
	weight_in_kg = float(input("Please enter Weight in Kg: "))
	height_in_cm = float(input("Now enter Height in Cm: "))
	height_in_m = height_in_cm / 100
	return weight_in_kg, height_in_m


def calculate_bmi(weight_in_kg, height_in_m):
	return round(weight_in_kg / height_in_m ** 2, 2)
	
def main():
	weight_in_kg, height_in_m = get_info()
	bmi = calculate_bmi(weight_in_kg, height_in_m)
	print(bmi)

main()
