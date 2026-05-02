def dot_product(tA, tB):
    """
    tA: a tuple of numbers
    tB: a tuple of numbers of the same length as tA
    Assumes tA and tB are the same length.
    Returns a tuple where the:
    * first element is the length of one of the tuples
    * second element is the sum of the pairwise products of tA and tB
    """

    numA = input("Digit some numbers separated by ',': ")
    numA = numA.split(",")
    numB = input("Digit numbers with the same size of the first input, separated by ',': ")
    numB = numB.split(",")
    
    result = 0
    for i in range(len(numA)):
        numA[i] = int(numA[i])
        numB[i] = int(numB[i])
        result += numA[i] * numB[i]
        
    tC = []
    tC.append(len(numA))
    tC.append(result)
    
    tC = tuple(tC)
    return tC
    
# Your code here
# Examples:
tA = (1, 2, 3)
tB = (4, 5, 6)
print(dot_product(tA, tB)) # prints (3,32)