def count_sqrts(l):
    count = 0
    for i in l:
        count += 1 if i*i in l else 0
    return count
print(count_sqrts([3,4,2,1,9,25])) # prints 3
