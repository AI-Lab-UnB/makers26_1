def part_a(yearly_salary, portion_saved, cost_of_dream_home):
	#########################################################################
	portion_down_payment = 0.25
	amount_saved = 0.0
	r = 0.05
	months = 0
	needed_value = cost_of_dream_home*portion_down_payment
	month_salary = year_salary/12
	month_add = portion_saved * month_salary
	
	
	###############################################################################################
	## Determine how many months it would take to get the down payment for your dream home below ## 
	###############################################################################################
	while amount_saved < needed_value:
	    amount_saved += amount_saved * (r/12)
	    amount_saved += month_add
	    months +=1
	
	print(f'Number of months: {months}')
	return months