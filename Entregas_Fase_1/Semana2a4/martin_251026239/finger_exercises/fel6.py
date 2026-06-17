n = int(input())

def binary_search(n):
    low = 0
    high = 1000

    while (low <= high):
        mid = low + (high - low) // 2

        if mid == n:
            return mid
        if mid < n:
            low = mid + 1
        else:
            high = mid - 1

print(binary_search(n))