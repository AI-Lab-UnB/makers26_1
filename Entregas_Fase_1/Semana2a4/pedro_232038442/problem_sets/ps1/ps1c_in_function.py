def part_c(initial_deposit):
	# Define constants
	low = 0.0
	high = 1.0
	epsilon = 100
	steps = 0
	target = 800000 * 0.25
	r = None

	# Determine the lowest rate of return needed to get the down payment for your dream home below
	if initial_deposit * (1 + high/12)**36 >= target - epsilon:
		while True:
			steps += 1
			r = (low + high) / 2
			savings = initial_deposit * (1 + r/12)**36
			if abs(savings - target) <= epsilon:
				break
			elif savings < target:
				low = r
			else:
				high = r
	else:
		r = None
		steps = 0
	
	if r is not None:
		print("Best savings rate:", r)
		print("Steps in bisection search:", steps)
	else:
		print("It is not possible to pay the down payment in three years.")
	return r, steps