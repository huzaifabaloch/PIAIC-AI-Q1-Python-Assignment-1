
"""
1
1 2
1 2 3
1 2 3 4 
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""

def make_pattern(size):
	
	# Counter for iteration.
	counter = 0
	# Start number traction.
	number = 0
	# It will add and remove numbers to make the desired pattern.
	lis = []
	
	while counter < size:
		lis.append(number+1)
		print(lis)
		counter += 1
		number += 1

	counter = size - 1
	while counter >= 1:
		del lis[counter]
		print(lis)
		counter -=1
    

make_pattern(10)
print("\n")
make_pattern(12)


 


