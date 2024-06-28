'''

Given an integer array representing a binary tree, where the parent-child relationship is defined by (A[i], i) for every index i in the array A, build a binary tree out of it. The root node's value is i if -1 is present at index i in the array.

Input: [-1, 0, 0, 1, 2, 2, 4, 4]

Output:

		   0
		 /   \
		/	  \
	   1	   2
	  /		  / \
	 /	  	 /	 \
	3		4	  5
		   / \
		  /   \
		 6	   7

Explanation:

• -1 is present at index 0, which implies that the binary tree root is node 0.
• 0 is present at index 1 and 2, which implies that the left and right children of node 0 are 1 and 2.
• 1 is present at index 3, which implies that the left or the right child of node 1 is 3.
• 2 is present at index 4 and 5, which implies that the left and right children of node 2 are 4 and 5.
• 4 is present at index 6 and 7, which implies that the left and right children of node 4 are 6 and 7.

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

def construct_binary_tree(parent: List[int]):
    if len(parent) == 0 or -1 not in parent:
        return None
    
    # construct nodes
    nodes = {i: Node(data=i) for i in range(len(parent))}

    # Connect nodes
    for i, p in enumerate(parent):
        if p == -1:
            root = nodes[i]
        elif p in nodes:
            if not nodes[p].left:
                nodes[p].left = nodes[i]
            else:
                nodes[p].right = nodes[i]

    return root

if __name__=="__main__":
    parent = [-1, 0, 0, 1, 2, 2, 4, 4]
    ans = construct_binary_tree(parent)
    print_tree(ans)
