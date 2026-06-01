def part_a(yearly_salary, portion_saved, cost_of_dream_home):
	#########################################################################
	
	portion_down_payment = 0.25
	amount_saved = 0.0
	annual_rate = 0.05
	months = 0
	
	###############################################################################################
	## Determine how many months it would take to get the down payment for your dream home below ## 
	###############################################################################################
	
	while(amount_saved < portion_down_payment * cost_of_dream_home):
	    amount_saved += amount_saved * annual_rate / 12
	    amount_saved += portion_saved * yearly_salary / 12
	    months += 1
	    
	print(f'Number of months: {months}')
	return months