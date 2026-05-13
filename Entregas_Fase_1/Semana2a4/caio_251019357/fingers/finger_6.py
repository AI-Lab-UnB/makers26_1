high = 1000
low = 0

calculate = (low + high) / 2

count = 1

N = 230

while calculate != N :

    if calculate < N or abs(low - calculate) == abs(high - calculate):

        low = calculate 

    elif calculate > N :

        high = calculate

    else :

        print(f"{count} iterations")
        print(f"N = {N}")

    count += 1

