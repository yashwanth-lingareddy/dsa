'''

Given the root of a binary search tree (BST), efficiently convert the BST into a min-heap. The solution should convert the given BST into a complete binary tree where each node has a higher value than its parent's value, using the same set of keys. The output binary tree should satisfy the structural and heap-ordering property of the min-heap data structure.

Input:
		 5
	   /   \
	  /		\
	 3		 8
	/ \		/ \
   /   \   /   \
  2		4 6	   10

Output:

		 2
	   /   \
	  /		\
	 3		 4
	/ \		/ \
   /   \   /   \
  5		6 8	   10

OR, any other valid min-heap.

Hint: 
1. convert BST to sorted array by level order traversal
2. convert sorted array to min heap

'''

from typing import List

class Node:
    def __init__(self, data = None, left=None, right=None) -> None:
        self.data = data	# data field
        self.left = left	# pointer to the left child
        self.right = right	# pointer to the right child

def build_tree():
    return Node(
        data=5,
        left=Node(
            data=3,
            left=Node(
                data=2
            ),
            right=Node(
                data=4
            )
        ),
        right=Node(
            data=8,
            left=Node(
                data=6
            ),
            right=Node(
                data=10
            )
        )
    )


def print_tree(root: Node, level: int):
    if root is None:
        return
    print_tree(root.right, level + 1)
    print('\t' * level + '|--' + str(root.data))
    print_tree(root.left, level + 1)

def in_order_traversal(root: Node):
    if not root:
        return []
    
    return in_order_traversal(root.left) + [root.data] + in_order_traversal(root.right)

def in_order_to_min_heap(i: int, inorder: List[int]):
    if i >= len(inorder):
        return None
    
    root = Node(data=inorder[i])
    root.left = in_order_to_min_heap(2 * i + 1, inorder)
    root.right = in_order_to_min_heap(2 * i + 2, inorder)
    return root

def bst_to_min_heap(root: Node) -> Node:
    inorder = in_order_traversal(root=root)
    min_heap = in_order_to_min_heap(0, inorder)
    return min_heap

if __name__=="__main__":
    root = build_tree()
    ans = bst_to_min_heap(root)
    print_tree(ans, 0)
