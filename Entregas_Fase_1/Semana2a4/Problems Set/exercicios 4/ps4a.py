# Problem Set 4A
# Name:
# Collaborators:

from tree import Node  # Imports the Node object used to construct trees

# Part A0: Data representation
# Fill out the following variables correctly.
# If correct, the test named test_data_representation should pass.

# arvore 1:
#      8
#    /   \
#   2     10
#  / \
# 1   6

tree1 = Node(8, Node(2, Node(1), Node(6)), Node(10))

# arvore 2:
#              7
#          /       \
#      2               9
#    /   \           /   \
#  1       5       8      10
#        /   \
#        3   6

tree2 = Node(7,
             Node(2, Node(1), Node(5, Node(3), Node(6))),
             Node(9, Node(8), Node(10)))

# arvore 3:
#              5
#          /       \
#      3               14
#    /   \           /    \
#  2       4       12      21
#                        /    \
#                       20    26

tree3 = Node(5,
             Node(3, Node(2), Node(4)),
             Node(14, Node(12), Node(21, Node(20), Node(26))))


def find_tree_height(tree):
    '''
    Find the height of the given tree
    Input:
        tree: An element of type Node constructing a tree
    Output:
        The integer depth of the tree
    '''
    # caso base: no folha tem altura 0
    if tree.get_left_child() is None and tree.get_right_child() is None:
        return 0

    alt_esq = -1
    alt_dir = -1

    if tree.get_left_child() is not None:
        alt_esq = find_tree_height(tree.get_left_child())

    if tree.get_right_child() is not None:
        alt_dir = find_tree_height(tree.get_right_child())

    # altura eh 1 + o maior caminho entre os filhos
    return 1 + max(alt_esq, alt_dir)


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
    esq = tree.get_left_child()
    dir = tree.get_right_child()

    # folha sempre satisfaz a propriedade
    if esq is None and dir is None:
        return True

    val_pai = tree.get_value()

    if esq is not None:
        if not compare_func(esq.get_value(), val_pai):
            return False
        if not is_heap(esq, compare_func):
            return False

    if dir is not None:
        if not compare_func(dir.get_value(), val_pai):
            return False
        if not is_heap(dir, compare_func):
            return False

    return True


if __name__ == '__main__':
    # You can use this part for your own testing and debugging purposes.
    # IMPORTANT: Do not erase the pass statement below if you do not add your own code
    pass
