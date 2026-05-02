def init_trees():
    tree1 = Node(8, Node(2, Node(1), Node(6)), Node(10))
    tree2 = Node(7, Node(2, Node(1), Node(5, Node(3), Node(6))), Node(9, Node(8), Node(10)))
    tree3 = Node(5, Node(3, Node(2), Node(4)), Node(14, Node(12), Node(21, Node(20), Node(26))))
    return tree1, tree2, tree3

def find_tree_height(tree):
    if tree.get_left_child() is None and tree.get_right_child() is None:
        return 0
        
    left_height = -1
    right_height = -1
    
    if tree.get_left_child() is not None:
        left_height = find_tree_height(tree.get_left_child())
        
    if tree.get_right_child() is not None:
        right_height = find_tree_height(tree.get_right_child())
        
    return 1 + max(left_height, right_height)

def is_heap(tree, compare_func):
    if tree is None:
        return True
        
    if tree.get_left_child() is None and tree.get_right_child() is None:
        return True
        
    left = tree.get_left_child()
    right = tree.get_right_child()
    parent_val = tree.get_value()
    
    is_valid = True
    
    if left is not None:
        if not compare_func(left.get_value(), parent_val):
            is_valid = False
        if not is_heap(left, compare_func):
            is_valid = False
            
    if right is not None:
        if not compare_func(right.get_value(), parent_val):
            is_valid = False
        if not is_heap(right, compare_func):
            is_valid = False
            
    return is_valid