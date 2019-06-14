
month_31 = [1, 3, 5, 7, 8, 10, 12]
month_30 = [4, 6, 9, 11]
counter = 0

day_operation = 0
month_operation = 0


months = [1,2,3,4,5,6,7,8,9,10,11,12]

date_1 = input("Enter date 1 in (dd/mm/yy) : ")
date_2 = input("Enter date 2 in (dd/mm/yy) : ")

date_1_split = date_1.split('/')
date_2_split = date_2.split('/')	

while counter < 3:
	
	if counter == 0:
		day_operation = int(date_1_split[counter]) - int(date_2_split[counter]) 
		print(day_operation)
		
		
	elif counter == 1:
		
		start_month = int(date_1_split[counter])
		end_month = int(date_2_split[counter])
		
		# Checking if starting and ending months are in months list.
		if start_month in months and end_month in months:
			
			"""
			Finding difference if start month greater than end month
			and adding one extra: Example start = october (10) and 
			end = april (4) 10 - 4 = 6, but we need to iterate through
			each month oct (1), sept(2), aug(3), july(4), june(5), 
			may(6), april(7).
			
			Else end month greater than start month and rest same as 
			above.  
			"""
			if start_month > end_month:
				month_difference = start_month - end_month
			
			else:
				month_difference = end_month - start_month
			
			# Checking continously month_differcnce if it is not 0.
			while month_difference != 0:
				"""
				if start month greater or equal than end_month, then 
				we checked for if that month is a 30 or 31 days month,
				if 30 we incrementing 31 and subtracting start_month
				so that we reach to end_month, or if it is a 30 days 
				month we adding 30 and decrementing start_month, and 
				we decrementing month_difference so we end the loop too.
				"""
				if start_month >= end_month:
					if start_month in month_31:
						month_operation += 31
						start_month -= 1
					
					elif start_month in month_30:
						month_operation += 30
						start_month -= 1
						
					else:
						month_operation += 28
				
				elif end_month >= start_month:
					if end_month in month_31:
						month_operation += 31
						end_month -= 1
						
					elif end_month in month_30:
						month_operation += 30
						end_month -= 1
						
					else:
						month_operation += 28
					
				
				month_difference -= 1
			
			if day_operation < 0:
				day_operation = str(day_operation)
				day_operation = day_operation.lstrip('-')
				total = month_operation + int(day_operation)
			else:
				total = month_operation - day_operation	
			print(month_operation)
			
	
	counter += 1
	
	
print('\n\n')
print("There are {} days".format(total))


