def dot_product(tA, tB):
    """
    tA: a tuple of numbers
    tB: a tuple of numbers of the same length as tA
    Assumes tA and tB have the same length.
    Returns a tuple where:
    * the first element is the length of one of the tuples
    * the second element is the sum of the pairwise products of tA and tB
    """
    
    return (len(tA), sum(a * b for a, b in zip(tA, tB)))

# Examples:
tA = (1, 2, 3)
tB = (4, 5, 6)
print(dot_product(tA, tB))  # prints (3, 32)