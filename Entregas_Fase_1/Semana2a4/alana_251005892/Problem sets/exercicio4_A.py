# Problem Set 4A
# Name:
# Collaborators:

from tree import Node # Imports the Node object used to construct trees

# Part A0: Data representation
# Fill out the following variables correctly.
# If correct, the test named test_data_representation should pass.
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
    # Base case: leaf node
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
    '''
    Determines if the tree is a max or min heap depending on compare_func
    Inputs:
        tree: An element of type Node constructing a tree
        compare_func: a function that compares the child node value to the parent node value
            i.e. op(child_value,parent_value) for a max heap would return True if child_value < parent_value and False otherwise
                 op(child_value,parent_value) for a min meap would return True if child_value > parent_value and False otherwise
    Output:
        True if the entire tree satisfies the compare_func function; False otherwise
    '''
    left = tree.get_left_child()
    right = tree.get_right_child()

    # Base case: leaf node is always a heap
    if left is None and right is None:
        return True

    parent_val = tree.get_value()

    if left is not None:
        if not compare_func(left.get_value(), parent_val):
            return False
        if not is_heap(left, compare_func):
            return False

    if right is not None:
        if not compare_func(right.get_value(), parent_val):
            return False
        if not is_heap(right, compare_func):
            return False

    return True



if __name__ == '__main__':
    # You can use this part for your own testing and debugging purposes.
    # IMPORTANT: Do not erase the pass statement below if you do not add your own code
    pass
