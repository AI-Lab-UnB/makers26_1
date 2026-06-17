# Problem Set 4A
# Name:
# Collaborators:

from tree import Node # Imports the Node object used to construct trees

# Part A0: Data representation
# Fill out the following variables correctly.
# If correct, the test named test_data_representation should pass.
tree1 = (Node(8, Node(2, Node(1), Node(6)) , Node(10)))
tree2 = Node(7, Node(2, Node(1), Node(5, Node(3), Node(6))), Node(9, Node(8), Node(10)))
tree3 = Node(5, Node(3, Node(2), Node(4)), Node(14, Node(12), Node(21, Node(20), Node(26))))
tr1 = Node(5, Node(7, Node(9, Node(10, Node(11)))))
tr2 = Node(5, right_child=Node(7, right_child=Node(9, right_child=Node(10, right_child=Node(11, right_child=Node(90,Node(2)))))))     
tr3 = Node(5)

def find_tree_height(tree):
    '''
    Find the height of the given tree
    Input:
        tree: An element of type Node constructing a tree
    Output:
        The integer depth of the tree
    '''
    
    if tree == None:
        return 0
    right = tree.get_right_child() 
    left = tree.get_left_child()
    if right == None and left == None:
        return 0
    return max(find_tree_height(right), find_tree_height(left)) + 1


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
    if tree is None:
        return True

    
    right = tree.get_right_child()
    left = tree.get_left_child()
    v1 = True
    v2 = True
    
    if right != None:
        v1 = compare_func(right.get_value(), tree.get_value())
    if left != None:
        v2 = compare_func(left.get_value(), tree.get_value())
    if(v1 and v2):
        return is_heap(right, compare_func) and is_heap(left, compare_func)
    else:
        return False



if __name__ == '__main__':
    # You can use this part for your own testing and debugging purposes.
    # IMPORTANT: Do not erase the pass statement below if you do not add your own code
    pass