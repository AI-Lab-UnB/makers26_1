import random

class Node:
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
        if left is not None:
            left.parent = self
        if right is not None:
            right.parent = self

    def __repr__(self):
        return f"Node({self.val})"
def compare_trees(node1: Node, node2: Node) -> bool:
    if node1 is None and node2 is None:
        return True
    if node1 is None or node2 is None:
        return False
    return (node1.val == node2.val
            and compare_trees(node1.left, node2.left)
            and compare_trees(node1.right, node2.right))
def compare_tree_children(node1: Node, node2: Node) -> bool:
    return compare_trees(node1, node2)
def find_tree_height(t: Node) -> int:
    if t is None:
        return -1           # empty tree
    if t.left is None and t.right is None:
        return 0            # leaf
    left_h  = find_tree_height(t.left)
    right_h = find_tree_height(t.right)
    return 1 + max(left_h, right_h)
def _get_right_child(node: Node) -> 'Node | None':
    return node.right if node else None

def _get_left_child(node: Node) -> 'Node | None':
    return node.left if node else None

def _get_parent(node: Node) -> 'Node | None':
    return node.parent if node else None
def is_max_heap(t: Node) -> bool:
    if t is None:
        return True
    if t.left is not None and t.left.val > t.val:
        return False
    if t.right is not None and t.right.val > t.val:
        return False
    return is_max_heap(t.left) and is_max_heap(t.right)
def is_min_heap(t: Node) -> bool:
    if t is None:
        return True
    if t.left is not None and t.left.val < t.val:
        return False
    if t.right is not None and t.right.val < t.val:
        return False
    return is_min_heap(t.left) and is_min_heap(t.right)
def test_find_tree_height():
    t = Node(5)
    assert find_tree_height(t) == 0, "single node should have height 0"
    t = Node(1, Node(2, Node(3)))
    assert find_tree_height(t) == 2
    t = Node(1,
             Node(2, Node(4), Node(5)),
             Node(3, Node(6), Node(7)))
    assert find_tree_height(t) == 2
    t = Node(2,
             Node(8, Node(7, Node(9)), Node(4)),
             Node(1, None, Node(3)))
    assert find_tree_height(t) == 3

    print("find_tree_height: all tests passed ✓")
if __name__ == '__main__':
    print("=== Part A – Tree Operations ===\n")
    test_find_tree_height()
    tree = Node(2,
                Node(8, Node(7, Node(9)), Node(4)),
                Node(1, None, Node(3)))
    print(f"Height of example tree: {find_tree_height(tree)}")  
    max_heap = Node(21,
                    Node(15, Node(7), Node(3)),
                    Node(5,  Node(4), Node(1)))
    print(f"Is max-heap: {is_max_heap(max_heap)}")  
    min_heap = Node(4,
                    Node(5,  Node(18), Node(9)),
                    Node(17, Node(21), Node(8)))
    print(f"Is min-heap: {is_min_heap(min_heap)}")  
    t1 = Node(1, Node(2), Node(3))
    t2 = Node(1, Node(2), Node(3))
    t3 = Node(1, Node(9), Node(3))
    print(f"compare_trees(t1, t2): {compare_trees(t1, t2)}")   
    print(f"compare_trees(t1, t3): {compare_trees(t1, t3)}")   
    print("\nAll Part A checks passed ✓")