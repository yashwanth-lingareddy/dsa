'''

Given two integer arrays representing inorder and level order traversal of a binary tree, construct and return the binary tree.

Input:

inorder[]    = [4, 2, 1, 7, 5, 8, 3, 6]
levelorder[] = [1, 2, 3, 4, 5, 6, 7, 8]

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

def print_tree(root: Node, level: int = 0):
    if root is None:
        return
    print_tree(root.right, level + 1)
    print('\t' * level + '|--' + str(root.data))
    print_tree(root.left, level + 1)


def construct_binary_tree(inorder: List[int], levelorder: List[int]) -> Node:
    # Write your code here...
    if len(inorder) == 0:
        return None
    if len(levelorder) == 0:
        return None
    
    # Check if that element exist in level order
    for i in range(0, len(levelorder)):

        if levelorder[i] in inorder:

            # Create a new node with
            # the matched element
            root = Node(levelorder[i])

            # Get the index of the matched element
            # in level order array
            io_index = inorder.index(levelorder[i])
            break

    # Construct left and right subtree
    root.left = construct_binary_tree(inorder[:io_index], levelorder)
    root.right = construct_binary_tree(inorder[io_index + 1:], levelorder)
    return root

if __name__=="__main__":
    inorder = [4, 2, 1, 7, 5, 8, 3, 6]
    levelorder = [1, 2, 3, 4, 5, 6, 7, 8]
    ans = construct_binary_tree(inorder, levelorder)
    print_tree(ans)