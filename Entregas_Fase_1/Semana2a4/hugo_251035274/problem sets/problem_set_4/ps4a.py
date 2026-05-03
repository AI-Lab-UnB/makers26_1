from tree import Node 

tree1 = Node(8, Node(2, Node(1), Node(6)), Node(10))
tree2 = Node(7, Node(2, Node(1), Node(5, Node(3), Node(6))), Node(9, Node(8), Node(10)))
tree3 = Node(5, Node(3, Node(2), Node(4)), Node(14, Node(12), Node(21, Node(20), Node(26))))

def find_tree_height(tree):
    if tree is None:
        return 0
    
    left_height = find_tree_height(Node.get_left_child(tree))
    right_height = find_tree_height(Node.get_right_child(tree))
    
    return max(left_height, right_height) + 1
    
def is_heap(tree, compare_func):
    if tree is None:
        return True
    
    if tree.left is None and tree.right is None:
        return True
    
    if tree.left:
        if not compare_func(tree.left.get_value(), tree.get_value()):
            return False
        if not is_heap(tree.left, compare_func):
            return False
    
    if tree.right:
        if not compare_func(tree.right.get_value(), tree.get_value()):
            return False
        if not is_heap(tree.right, compare_func):
            return False
        
    return True

def compare_func(child_value, parent_value):
    if child_value < parent_value:
        return True
    return False    

if __name__ == '__main__':
    print(find_tree_height(tree1))
    print(find_tree_height(tree2))
    print(find_tree_height(tree3))
    
    print(is_heap(tree1, compare_func))
    print(is_heap(tree2, compare_func))
    print(is_heap(tree3, compare_func))
    
    tree4 = Node(50, Node(30), Node(40))
    
    print(is_heap(tree4, compare_func))
