def running_product(a):
    """ a é um inteiro """
    product = 1                       # O(1)
    for i in range(5, a + 5):         # Repete 'a' vezes (n vezes)
        product *= i                  # O(1)
        if product == a:              # O(1)
            return True               # O(1)
    return False                      # O(1)

# Big-O: O(n)