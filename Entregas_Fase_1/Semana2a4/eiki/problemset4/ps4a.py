# Problem Set 4A
# Name: Matheus Eiki
# Collaborators:
 
from tree import Node 
 
# Part A0: Data representation
tree1 = Node(8, Node(2, Node(1), Node(6)), Node(10))
tree2 = Node(7, Node(2, Node(1), Node(5, Node(3), Node(6))), Node(9, Node(8), Node(10)))
tree3 = Node(5, Node(3, Node(2), Node(4)), Node(14, Node(12), Node(21, Node(20), Node(26))))
 
 
def find_tree_height(tree):
    '''
    Find the height of the given tree
    Input:
        tree: An element of type Node constructing a tree
    Output:
        The integer depth of the tree
    '''
    if tree.get_left_child() is None and tree.get_right_child() is None:
        return 0
    left_height = find_tree_height(tree.get_left_child()) if tree.get_left_child() is not None else -1
    right_height = find_tree_height(tree.get_right_child()) if tree.get_right_child() is not None else -1
    return 1 + max(left_height, right_height)
 
 
def is_heap(tree, compare_func):
    '''
    Determines if the tree is a max or min heap depending on compare_func
    Inputs:
        tree: An element of type Node constructing a tree
        compare_func: a function that compares the child node value to the parent node value
    Output:
        True if the entire tree satisfies the compare_func function; False otherwise
    '''

    if tree.get_left_child() is None and tree.get_right_child() is None:
        return True

    if tree.get_left_child() is not None:
        if not compare_func(tree.get_left_child().get_value(), tree.get_value()):
            return False
        if not is_heap(tree.get_left_child(), compare_func):
            return False
  
    if tree.get_right_child() is not None:
        if not compare_func(tree.get_right_child().get_value(), tree.get_value()):
            return False
        if not is_heap(tree.get_right_child(), compare_func):
            return False
    return True
 
 
if __name__ == '__main__':
    pass