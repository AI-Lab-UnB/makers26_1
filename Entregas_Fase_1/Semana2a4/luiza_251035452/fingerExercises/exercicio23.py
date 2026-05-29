# Questão 1: running_product(a)   -   n = a

# for i in range(5, a+5):    loop executa 'a' vezes
#     product *= i            O(1)
#     if product == a:       
#         return True        
# return False               

# Resposta:
theta_q1 = "O(n)"  # linear
 
# Questão 2: tricky_f(L, L2)   -   n = len(L)

# for e1 in L:           
#     if e1 in L2:       

# for e2 in L2:          
#     if e2 in L:        
# Total: n*n + n*n = 2n²  

# Resposta:
theta_q2 = "O(n²)"  # quadrático

# Questão 3: sum_f(n)
# while n > 0:
#     answer += n % 10   
#     n = int(n / 10)    
# Número de iterações = número de dígitos de n

# Resposta:
theta_q3 = "O(log n)"  # logarítmico