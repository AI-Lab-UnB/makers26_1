def running_product(a):
    product = 1
    for i in range(5, a+5):
        product *= i
        if product == a:
            return True
    return False