def part_c(initial_deposit):
	#########################################################################
	custo_casa = 800000
	entrada_necessaria = 0.25 * custo_casa
	meses = 36
	
	##################################################################################################
	## Determine the lowest rate of return needed to get the down payment for your dream home below ##
	##################################################################################################
	if initial_deposit >= entrada_necessaria - 100:
	    r = 0.0
	    steps = 0
	else:
	    valor_maximo = initial_deposit * (1 + 1.0 / 12) ** meses
	    if valor_maximo < entrada_necessaria - 100:
	        r = None
	        steps = 0
	    else:
	        baixo = 0.0
	        alto = 1.0
	        r = (baixo + alto) / 2
	        steps = 1
	
	        while True:
	            valor_guardado = initial_deposit * (1 + r / 12) ** meses
	            diferenca = valor_guardado - entrada_necessaria
	
	            if abs(diferenca) < 100:
	                break
	
	            steps += 1
	
	            if diferenca < 0:
	                baixo = r
	            else:
	                alto = r
	
	            r = (baixo + alto) / 2
	
	print("Best savings rate:", r)
	print("Steps in bisection search:", steps)
	return r, steps