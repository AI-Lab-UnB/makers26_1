def part_a(yearly_salary, portion_saved, cost_of_dream_home):
	# Define constants
	portion_down_payment = 0.25
	current_savings = 0.0
	r = 0.05
	monthly_salary = yearly_salary / 12
	months = 0	

	# Determine how many months it would take to get the down payment for your dream home below
	while current_savings < cost_of_dream_home * portion_down_payment:
		current_savings += current_savings * r / 12 + portion_saved * monthly_salary
		months += 1

	print("Number of months:", months)
	return months