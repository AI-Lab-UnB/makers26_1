def sum_f(n):
    answer = 0
    while n > 0:
        answer += n % 10
        n = int(n / 10)
    return answer