import math

n = int(input())
sqrt = int(math.sqrt(n))

if isinstance(sqrt, int):
    print(sqrt)
else:
    print("error")