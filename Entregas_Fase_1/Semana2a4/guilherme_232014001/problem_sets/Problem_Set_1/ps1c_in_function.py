def part_c(initial_deposit):
	#########################################################################
	months = 36
	cost_of_dream_home = 800000
	portion_down_payment = 0.25
	down_payment = cost_of_dream_home * portion_down_payment
	
	low = 0.0
	high = 1.0
	r = None
	steps = 0
	
	##################################################################################################
	## Determine the lowest rate of return needed to get the down payment for your dream home below ##
	##################################################################################################
	if initial_deposit * (1 + 1.0 / 12) ** months < down_payment:
	    r = None
	    steps = 0
	
	# caso ja tem dinheiro suficiente sem nenhuma taxa
	elif initial_deposit >= down_payment:
	    r = 0.0
	    steps = 0
	
	else:
	    while True:
	        r = (low + high) / 2
	        savings = initial_deposit * (1 + r / 12) ** months
	        steps += 1
	
	        if abs(savings - down_payment) <= 100:
	            break
	        elif savings < down_payment:
	            low = r
	        else:
	            high = r
	
	print("Best rate of return:", r)
	print("Steps in bisection search:", steps)
	
	return r, steps