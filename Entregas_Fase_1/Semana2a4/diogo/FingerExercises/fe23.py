# Question 1: Choose the worst-case asymptotic order of growth (upper and lower bound) for the following function. Assume n = a.

def running_product(a):
    """ a is an int """
    product = 1
    for i in range(5,a+5):
        product *= i
        if product == a:
            return True
    return False

# Big O(n/5) = Big O(n)

# Question 2: Choose the worst-case asymptotic order of growth (upper and lower bound) for the following function. Assume n = len(L).

def tricky_f(L, L2):
    """ L and L2 are lists of equal length """
    inL = False
    for e1 in L:
        if e1 in L2:
            inL = True
            
    inL2 = False
    for e2 in L2:
        if e2 in L:
            inL2 = True

    return inL and inL2

# --- Big O(2 * n^2) = Big O(n^2) ---

# Question 3: Choose the worst-case asymptotic order of growth (upper and lower bound) for the following function.

def sum_f(n):
    """ n > 0 """
    answer = 0
    while n > 0:
        answer += n%10
        n = int(n/10)
    return answer

# Big O( log(N) )
