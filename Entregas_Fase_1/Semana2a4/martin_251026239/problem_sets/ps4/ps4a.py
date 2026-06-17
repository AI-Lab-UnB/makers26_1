from tree import Node # Imports the Node object used to construct trees

# Part A0: Data representation
# Fill out the following variables correctly.
# If correct, the test named test_data_representation should pass.
tree1 = Node(8, Node(2, node(1), Node(6)), Node(10))
tree2 = Node(7, Node(2, Node(1), Node(5, Node(3), Node(6))), Node(9, Node(8), Node(10)))
tree3 = Node(5, Node(3, Node(2), Node(4)), Node(14, Node(12), Node(21, Node(20), Node(26))))

def find_tree_height(tree):
    if tree.get_left_child() is None and tree.get_right_child() is None:
        return 0
    
    altura_esq = 0
    altura_dir = 0

    if tree.get_left_child() is not None:
        altura_esq = find_tree_height(tree.get_left_child())
    if tree.get_right_child() is not None:
        altura_dir = find_tree_height(tree.get_right_child())

    return 1 + max(altura_esq, altura_dir)


def is_heap(tree, compare_func):

    if tree is None:
        return True
        
    if tree.get_left_child() is None and tree.get_right_child() is None:
        return True
        
    esq_valido = True
    dir_valido = True

    if tree.get_left_child() is not None:
        valor_filho = tree.get_left_child().get_value()
        valor_pai = tree.get_value()
        
        if not compare_func(valor_filho, valor_pai):
            return False
            
        esq_valido = is_heap(tree.get_left_child(), compare_func)

    if tree.get_right_child() is not None:
        valor_filho = tree.get_right_child().get_value()
        valor_pai = tree.get_value()
        
        if not compare_func(valor_filho, valor_pai):
            return False
            
        dir_valido = is_heap(tree.get_right_child(), compare_func)

    return esq_valido and dir_valido



if __name__ == '__main__':
    
    print("Altura da tree1:", find_tree_height(tree1))
    
    def compare_max(child_value, parent_value):
        return child_value < parent_value
        
    def compare_min(child_value, parent_value):
        return child_value > parent_value

    print("tree1 é max heap?", is_heap(tree1, compare_max))
    print("tree1 é min heap?", is_heap(tree1, compare_min))
