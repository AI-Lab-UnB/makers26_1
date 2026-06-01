def sum_f(n):
    """ n > 0 """
    answer = 0                # O(1)
    while n > 0:              # Repete 'k' vezes
        answer += n % 10      # O(1)
        n = int(n / 10)       # O(1)
    return answer

# Big-O: O(k), onde k é o número de dígitos de n