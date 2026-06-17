Lista = [1, 2, 4, 8]
k = 2


def remove_and_sort(Lin, k):
    for c in range(k):
        del Lin[0]
    Lin.sort()
    print(Lin)

remove_and_sort(Lista,k)      