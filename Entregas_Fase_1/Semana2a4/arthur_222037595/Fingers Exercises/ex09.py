# Finger Exercise - Lecture 9
# Name: Arthur Carvalho Leite
# Matrícula: 222037595

def dot_product(tA, tB):
    """
    tA: a tuple of numbers
    tB: a tuple of numbers of the same length as tA
    Assumes tA and tB are the same length.
    Returns a tuple where the:
    * first element is the length of one of the tuples
    * second element is the sum of the pairwise products of tA and tB
    """
    soma = 0
    for i in range(len(tA)):
        soma += tA[i] * tB[i]
    return (len(tA), soma)
