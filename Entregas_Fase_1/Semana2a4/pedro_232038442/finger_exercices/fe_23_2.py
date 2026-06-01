def tricky_f(L, L2):
    """ L e L2 são listas de mesmo comprimento """
    inL = False                       # O(1)
    for e1 in L:                      # Repete 'n' vezes
        if e1 in L2:                  # O(n) -> Busca em lista
            inL = True                # O(1)
    inL2 = False                      # O(1)
    for e2 in L2:                     # Repete 'n' vezes
        if e2 in L:                   # O(n) -> Busca em lista
            inL2 = True               # O(1)
    return inL and inL2               # O(1)

# Big-O: O(n^2)