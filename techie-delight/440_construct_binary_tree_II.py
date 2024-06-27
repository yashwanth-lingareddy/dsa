'''

Given two integer arrays representing inorder and postorder traversal of a binary tree, construct and return the binary tree.

Input:

inorder[]   = [4, 2, 1, 7, 5, 8, 3, 6]
postorder[] = [4, 2, 7, 8, 5, 6, 3, 1]

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
    def __init__(self, data = None, left=None, right=None) -> None:
        self.data = data	# data field
        self.left = left	# pointer to the left child
        self.right = right	# pointer to the right child

def print_tree(root: Node, level: int = 0):
    if root is None:
        return
    print_tree(root.right, level + 1)
    print('\t' * level + '|--' + str(root.data))
    print_tree(root.left, level + 1)


def construct_binary_tree(inorder: List[int], postorder: List[int]):
    if len(inorder) == 0:
        return None
    
    if len(postorder) == 0:
        return None
        
    root = Node(data=postorder[len(postorder) - 1])
    mid = inorder.index(postorder[len(postorder) - 1])
    
    root.left = construct_binary_tree(inorder[:mid], postorder[:mid])
    root.right = construct_binary_tree(inorder[mid+1:], postorder[mid:-1])
    
    return root

if __name__=="__main__":
    inorder = [4, 2, 1, 7, 5, 8, 3, 6]
    postorder = [4, 2, 7, 8, 5, 6, 3, 1]
    ans = construct_binary_tree(inorder, postorder)
    print_tree(ans)
