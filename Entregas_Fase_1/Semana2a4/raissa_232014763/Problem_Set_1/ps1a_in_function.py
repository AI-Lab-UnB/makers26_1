def part_a(yearly_salary, portion_saved, cost_of_dream_home):
	#########################################################################
	savings = 0
	months = 0
	portion_of_payment = 0.25
	down_payment = portion_of_payment * cost_of_dream_home
	
	###############################################################################################
	## Determine how many months it would take to get the down payment for your dream home below ## 
	###############################################################################################
	while savings < down_payment:
	    savings += savings * (0.05 / 12) + (yearly_salary / 12) * portion_saved
	    months += 1
	
	print("Number of months:", months)
	return months