# Problem Set 4A
# Name: Diogo Oliveira
# Collaborators: Diogo Oliveira

from tree import Node # Imports the Node object used to construct trees

# Part A0: Data representation
# Fill out the following variables correctly.
# If correct, the test named test_data_representation should pass.
tree1 = Node(8, Node(2, Node(1), Node(6)),  Node(10) )
tree2 = Node(7, Node(2, Node(1), Node(5,    Node(3), Node(6))), Node(9, Node(8), Node(10)) )
tree3 = Node(5, Node(3, Node(2), Node(4)),  Node(14, Node(12), Node(21, Node(20), Node(26))) )

def find_tree_height(tree : Node):
    
    if  tree == None:
        return -1
    
    left_height  = 1 + find_tree_height(tree.get_left_child())
    right_height = 1 + find_tree_height(tree.get_right_child())
    
    return max(left_height, right_height)

# Max heap comparator
def compare_func(child_value, parent_value):
    if child_value < parent_value:
       return True
    return False

def is_heap(tree : Node, compare_func):

    if tree == None: # Leaf
        return True
    
    if(tree.get_left_child() != None):
        is_left_heap = compare_func(tree.get_left_child().get_value(), tree.get_value())
        if(not is_left_heap):
            return False
        
    if(tree.get_right_child() != None):
        is_right_heap = compare_func(tree.get_right_child().get_value(), tree.get_value())
        if(not is_right_heap):
            return False
    
    return is_heap(tree.get_left_child(), compare_func) and is_heap(tree.get_right_child(), compare_func)


if __name__ == '__main__':
    
    print(find_tree_height(tree1)) # should be 2
    print(find_tree_height(tree2)) # should be 3
    print(find_tree_height(tree3)) # should be 3
    
    # Max heap test cases
    tr1 = Node(15,Node(4,Node(3,None,Node(2)),Node(1)),Node(11,Node(10),Node(7,Node(5))))
    tr2 = Node(10,Node(7,None,Node(4,Node(3,None,Node(5)))))
    
    print(is_heap(tr1, compare_func)) # should return True
    print(is_heap(tr2, compare_func)) # should return False
