# Problem Set 4A
# Name:
# Collaborators:

from tree import Node # Imports the Node object used to construct trees

# Part A0: Data representation
# Fill out the following variables correctly.
# If correct, the test named test_data_representation should pass.
tree1 = Node(8, Node(2, Node(1), Node(6)), Node(10))
tree2 = Node(7, Node(2, Node(1), Node(5, Node(3), Node(6))), Node(9, Node(8), Node(10)))
tree3 = Node(5, Node(3,Node(2), Node(4)), Node(14, Node(12), Node(21, Node(20), Node(26))))

#MIn :

tree_min_1 = Node(5,Node(15,None,Node(16,Node(30),Node(17))),Node(6,Node(20,None,Node(45)),Node(11)))
tree_min_2 = Node(2,Node(3,Node(4),Node(5,Node(6))),Node(7,None,Node(8,Node(9),Node(1))))

#max

tree_max_1 = Node(15,Node(4,Node(3,None,Node(2)),Node(1)),Node(11,Node(10),Node(7,Node(5))))
tree_max_2 = Node(10,Node(7,None,Node(4,Node(3,None,Node(5)))))


def find_tree_height(tree):
    
    # tree = print(tree.get_value())
    # tree = print(tree.get_left_child())
    # tree = print(tree.get_right_child())

    # print(tree)

    if tree is None :
        return -1
    
    else :

        left = find_tree_height(tree.get_left_child())
        right = find_tree_height(tree.get_right_child())

        # tree = print(tree.get_left_child())
        # tree = print(tree.get_right_child())

        return 1 + max(left, right)





def is_heap(tree, compare_func):


    if tree is None or (tree.get_left_child() is None and tree.get_right_child() is None):
        return True

    if tree.get_left_child():
        if not compare_func(tree.get_left_child().get_value(), tree.get_value()):
            return False
        if not is_heap(tree.get_left_child(), compare_func):
            return False

    if tree.get_right_child():
        if not compare_func(tree.get_right_child().get_value(), tree.get_value()):
            return False
        if not is_heap(tree.get_right_child(), compare_func):
            return False
        
    return True
    



if __name__ == '__main__':
    # You can use this part for your own testing and debugging purposes.
    # IMPORTANT: Do not erase the pass statement below if you do not add your own code
    # print(is_heap(tree_min_1, compare_func(tree_min_1)))

    # print(compare_func = lambda x,y: x < y)
    #st_tr1 = student.is_heap(tr1,compare_func)
    pass