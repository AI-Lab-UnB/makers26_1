def part_b(yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise):
	#########################################################################
	savings = 0
	months = 0
	portion_down_payment = 0.25
	down_payment = cost_of_dream_home * portion_down_payment
	annual_return = 0.05
	
	
	###############################################################################################
	## Determine how many months it would take to get the down payment for your dream home below ## 
	###############################################################################################
	while savings < down_payment:
	    savings += savings * (annual_return / 12) + (yearly_salary / 12) * portion_saved
	    months += 1
	    if months % 6 == 0:
	        yearly_salary *= (1 + semi_annual_raise)
	
	print("Number of months:", months)
	return months