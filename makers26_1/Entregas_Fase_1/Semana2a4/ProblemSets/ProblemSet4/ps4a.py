# Problem Set 4A
# Name:
# Collaborators:

from tree import Node # Imports the Node object used to construct trees

# Part A0: Data representation
# Fill out the following variables correctly.
# If correct, the test named test_data_representation should pass.
tree1 = None #TODO
tree2 = None #TODO
tree3 = None #TODO

def find_tree_height(tree):
    if tree is None:
        return -1
    
    if tree.get_left_child() is None and tree.get_right_child() is None:
        return 0
    
    leftValue = find_tree_height(tree.get_left_child())
    rightValue= find_tree_height(tree.get_right_child())

    return 1 + max(leftValue,rightValue)


def is_heap(tree, compare_func):
    
    if tree is None:
        return True
    
    parent_val = tree.get_value()
    left_child = tree.get_left_child()
    right_child = tree.get_right_child()

    if left_child is not None:
        if not compare_func(left_child.get_value(), parent_val):
            return False
       
    if right_child is not None:
        if not compare_func(right_child.get_value(), parent_val):
            return False

    return is_heap(left_child, compare_func) and is_heap(right_child, compare_func)



if __name__ == '__main__':
    # You can use this part for your own testing and debugging purposes.
    # IMPORTANT: Do not erase the pass statement below if you do not add your own code
    pass
