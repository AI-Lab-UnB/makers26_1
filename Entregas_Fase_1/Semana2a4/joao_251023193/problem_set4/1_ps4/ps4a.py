# Problem Set 4A
# Name: João Vítor Sauma de Faria
# Collaborators:

from tree import Node # Imports the Node object used to construct trees

# Part A0: Data representation
# Fill out the following variables correctly.
# If correct, the test named test_data_representation should pass.
tree1 = None #TODO
tree2 = None #TODO
tree3 = None #TODO


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
    # TODO: Remove pass and write your code here

    
    #Base Case
    if tree is None:
        return -1
    
    #Recursive Case
    left_height = find_tree_height(tree.get_left_child())
    right_height = find_tree_height(tree.get_right_child())
    
    return 1 + max(left_height, right_height)
    
    pass

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
    # TODO: Remove pass and write your code here
    
    
    
    '''um nó é um heap se ele respeita a regra com seus filhos e se seus filhos também são heap'''
    
    #Base Case
    #If the tree is empty = True
    #If the tree is leaf = True
    if tree is None:
        return True
    
    if tree.get_left_child() is None and tree.get_right_child() is None:
        return True
    
    #Recursive Case
    #Checking if left child exists
    left_child = tree.get_left_child()
    if tree.get_left_child() is not None: 
        
        if not compare_func(left_child.get_value(), tree.get_value()):
            return False
        
        if not is_heap(left_child, compare_func):
            return False
        
    
    #Checking if right child exists
    right_child = tree.get_right_child()
    if tree.get_right_child() is not None:
        
        if not compare_func(right_child.get_value(), tree.get_value()):
            return False
            
        if not is_heap(right_child, compare_func):
            return False
        
    return True
        
        
            
        
            

        
    
    



if __name__ == '__main__':
    # You can use this part for your own testing and debugging purposes.
    # IMPORTANT: Do not erase the pass statement below if you do not add your own code
    
    
    
    pass
