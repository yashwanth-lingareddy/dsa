'''

Given two integer arrays representing inorder and preorder traversal of a binary tree, construct and return the binary tree.

Input:


preorder[] = [1, 2, 4, 3, 5, 7, 8, 6]
inorder[]  = [4, 2, 1, 7, 5, 8, 3, 6]

Output: Root of below binary tree

		   1
		 /   \
		/	  \
	   2	   3
	  /		  / \
	 /	  	 /	 \
	4		5	  6
		   / \
		  /   \
		 7	   8

'''
from typing import List

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data	# data field
        self.left = left	# pointer to the left child
        self.right = right	# pointer to the right child

def print_tree(root: Node, level: int):
    if root is None:
        return
    print_tree(root.right, level + 1)
    print('\t' * level + '|--' + str(root.data))
    print_tree(root.left, level + 1)

def construct_binary_tree(inorder: List[int], preorder: List[int]) -> Node:
    if len(inorder) == 0:
        return None
    
    if len(preorder) == 0:
        return None
    
    # first value of preorder array is always the root of the tree
    root = Node(data=preorder[0])
    
    # Now figure out left and right of root using inorder
    # preorder[] = [1, 2, 4, 3, 5, 7, 8, 6]
    # inorder[]  = [4, 2, 1, 7, 5, 8, 3, 6]
    # left
    # preorder[] = [2, 4]
    # inorder[] = [4, 2]
    # right
    # preorder[] = [3, 5, 7, 8, 6]
    # inorder[] = [7, 5, 8, 3, 6]
    mid = inorder.index(preorder[0])
		
    root.left = construct_binary_tree(inorder[:mid], preorder[1:mid+1])
    root.right = construct_binary_tree(inorder[mid+1:], preorder[mid+1:])

    return root

if __name__=="__main__":
    preorder = [1, 2, 4, 3, 5, 7, 8, 6]
    inorder  = [4, 2, 1, 7, 5, 8, 3, 6]
    root = construct_binary_tree(inorder, preorder)
    print(print_tree(root, 0))
