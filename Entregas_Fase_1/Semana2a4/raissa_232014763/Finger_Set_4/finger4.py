N = 27

counter = 0
while counter ** 3 < N:
    counter += 1

if counter ** 3 == N:
    print(counter)
else:
    print("error")