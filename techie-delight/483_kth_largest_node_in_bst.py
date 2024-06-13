'''

Given the root of a binary search tree (BST) and a positive number k, find the k'th largest node in the BST.

For example, consider the following BST.

		  15
		/	 \
	   /	  \
	  /		   \
	 10		   20
	/  \	  /  \
   /	\	 /	  \
  8		12	16	  25

Input: k = 4
Output: Node 15

Input: k = 2
Output: Node 20

The solution should return None if k is more than number of nodes in the BST.

Input: k = 8
Output: None

'''

from typing import List

class Node:
    def __init__(self, data = None, left=None, right=None) -> None:
        self.data = data	# data field
        self.left = left	# pointer to the left child
        self.right = right	# pointer to the right child

def print_tree(root: Node, level: int):
    if root is None:
        return
    print_tree(root.right, level + 1)
    print('\t' * level + '|--' + str(root.data))
    print_tree(root.left, level + 1)

def build_tree():
    return Node(
        data=15,
        left=Node(
            data=10,
            left=Node(
                data=8
            ),
            right=Node(
                data=12
            )
        ),
        right=Node(
            data=20,
            left=Node(
                data=16
            ),
            right=Node(
                data=25
            )
        )
    )

def in_order_traversal(root: Node, path: List[Node]):
    if root is None:
        return
    
    in_order_traversal(root.left, path)
    path.append(root)
    in_order_traversal(root.right, path)

def kth_largest_node(root: Node, k: int):
    path = []
    in_order_traversal(root, path)

    if k > len(path):
        return None
    
    return path[len(path) - k]

if __name__=="__main__":
    root = build_tree()
    k = 2
    ans = kth_largest_node(root, k)
    print_tree(ans, 0)