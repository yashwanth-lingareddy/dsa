'''

Given a sequence of distinct keys representing the preorder traversal of a binary search tree (BST), construct and return a BST out of the sequence.

Input: [15, 10, 8, 12, 20, 16, 25]

Output:
		  15
		/	 \
	   /	  \
	  /		   \
	 10		   20
	/  \	  /  \
   /	\	 /	  \
  8		12	16	  25

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

def construct_bst(preorder: List[int]):
    if len(preorder) == 0:
        return None
    
    root = Node(data=preorder[0])
    i = 1
    # all the values to the left of the root node are less than the root node in BST
    # itereate in preorder until the values are less than root
    while i < len(preorder) and root.data > preorder[i]:
        i += 1
    
    root.left = construct_bst(preorder[1:i])
    root.right = construct_bst(preorder[i:])
    return root

if __name__=="__main__":
    preorder = [15, 10, 8, 12, 20, 16, 25]
    ans = construct_bst(preorder)
    print_tree(ans, 0)