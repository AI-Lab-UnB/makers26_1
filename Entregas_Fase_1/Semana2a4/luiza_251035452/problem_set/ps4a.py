from tree import Node

tree1 = Node(8,
             Node(2, Node(1), Node(6)),
             Node(10))

tree2 = Node(7,
             Node(2, Node(1), Node(5, Node(3), Node(6))),
             Node(9, Node(8), Node(10)))

tree3 = Node(5,
             Node(3, Node(2), Node(4)),
             Node(14, Node(12), Node(21, Node(20), Node(26))))




def find_tree_height(tree):
    if tree.get_left_child() is None and tree.get_right_child() is None:
        return 0
    altura_esq = find_tree_height(tree.get_left_child()) if tree.get_left_child() else -1
    altura_dir = find_tree_height(tree.get_right_child()) if tree.get_right_child() else -1
    return 1 + max(altura_esq, altura_dir)



def comparador_max(valor_filho, valor_pai):
    if valor_filho < valor_pai:
        return True
    return False

def comparador_min(valor_filho, valor_pai):
    if valor_filho > valor_pai:
        return True
    return False

def is_heap(tree, compare_func):
    if tree.get_left_child() is None and tree.get_right_child() is None:
        return True
    esq = tree.get_left_child()
    dir = tree.get_right_child()
    if esq is not None:
        if not compare_func(esq.get_value(), tree.get_value()):
            return False
        if not is_heap(esq, compare_func):
            return False
    if dir is not None:
        if not compare_func(dir.get_value(), tree.get_value()):
            return False
        if not is_heap(dir, compare_func):
            return False
    return True


print(find_tree_height(tree1))  
print(find_tree_height(tree2))  
print(find_tree_height(tree3))  

heap_max = Node(21, Node(15, Node(7), Node(11)), Node(3, Node(2), Node(1)))
print(is_heap(heap_max, comparador_max)) 

heap_min = Node(4, Node(10, Node(18), Node(11)), Node(5, Node(7), Node(8)))
print(is_heap(heap_min, comparador_min))  