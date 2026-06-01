

'''
LINHA DE PENSAMENTO:
- PARTE 1: representar as arvores usando o objeto Node
- PARTE 2: calcular a altura da arvore recursivamente
- PARTE 3: verificar se a arvore e um heap (max ou min)
'''

from tree import Node

# REPRESENTACAO DAS ARVORES
# cada Node recebe (valor, filho_esquerdo, filho_direito)
# folhas sao nodes sem filhos
tree1 = Node(8,
             Node(2, Node(1), Node(6)),
             Node(10))

tree2 = Node(7,
             Node(2, Node(1), Node(5, Node(3), Node(6))),
             Node(9, Node(8), Node(10)))

tree3 = Node(5,
             Node(3, Node(2), Node(4)),
             Node(14,
                  Node(12),
                  Node(21, Node(20), Node(26))))

# PARTE 2 - ALTURA DA ARVORE
# calcula a altura recursivamente
# caso base: folha tem altura 0
# caso recursivo: 1 + max(altura esquerda, altura direita)
def find_tree_height(arvore):
    # caso base - se nao tem filhos e uma folha com altura 0
    if arvore.get_left_child() is None and arvore.get_right_child() is None:
        return 0

    # inicializa as alturas dos filhos
    altura_esquerda = -1
    altura_direita = -1

    # calcula recursivamente a altura de cada filho existente
    if arvore.get_left_child() is not None:
        altura_esquerda = find_tree_height(arvore.get_left_child())
    if arvore.get_right_child() is not None:
        altura_direita = find_tree_height(arvore.get_right_child())

    # retorna 1 + a maior altura entre os dois filhos
    return 1 + max(altura_esquerda, altura_direita)

# PARTE 3 - VERIFICAR SE E UM HEAP
# verifica recursivamente se a arvore e max heap ou min heap
# caso base: folha sempre e um heap
# caso recursivo: verifica se os filhos satisfazem a condicao do heap
def is_heap(arvore, compare_func):
    filho_esquerdo = arvore.get_left_child()
    filho_direito = arvore.get_right_child()

    # caso base - folha sempre e um heap
    if filho_esquerdo is None and filho_direito is None:
        return True

    # verifica filho esquerdo
    if filho_esquerdo is not None:
        # checa se a relacao pai-filho satisfaz a condicao
        if not compare_func(filho_esquerdo.get_value(), arvore.get_value()):
            return False
        # verifica recursivamente a subarvore esquerda
        if not is_heap(filho_esquerdo, compare_func):
            return False

    # verifica filho direito
    if filho_direito is not None:
        # checa se a relacao pai-filho satisfaz a condicao
        if not compare_func(filho_direito.get_value(), arvore.get_value()):
            return False
        # verifica recursivamente a subarvore direita
        if not is_heap(filho_direito, compare_func):
            return False

    return True
if __name__ == '__main__':
    # testando altura das arvores
    print('Altura tree1:', find_tree_height(tree1))  # deve ser 2
    print('Altura tree2:', find_tree_height(tree2))  # deve ser 3
    print('Altura tree3:', find_tree_height(tree3))  # deve ser 3

    # testando is_heap com max heap
    max_heap = Node(21, Node(15, Node(7), Node(11)), Node(3, Node(2), Node(1)))
    compare_max = lambda filho, pai: filho < pai
    print('Max heap valido:', is_heap(max_heap, compare_max))  # deve ser True

    # testando is_heap com min heap
    min_heap = Node(4, Node(10, Node(18), Node(11)), Node(5, Node(7), Node(8)))
    compare_min = lambda filho, pai: filho > pai
    print('Min heap valido:', is_heap(min_heap, compare_min))  # deve ser True

    # testando heap invalido
    heap_invalido = Node(5, Node(10), Node(3))
    print('Heap invalido (max):', is_heap(heap_invalido, compare_max))  # deve ser False