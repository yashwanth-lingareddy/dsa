'''

Given an integer array representing preorder traversal of a binary tree, and a boolean array that determines if the value at the corresponding index in the preorder sequence is a leaf node or an internal node, construct and return the full binary tree. A full binary tree is a tree in which every node has either 0 or 2 children.

Input:

preorder[] = [1, 2, 4, 5, 3, 6, 8, 9, 7]
isLeaf[]   = [0, 0, 1, 1, 0, 0, 1, 1, 1]	 (1 represents a leaf node, and 0 represents an internal node)

Output: Root of below binary tree

		   1
		 /   \
		/	  \
	   2	   3
	  /	\	  / \
	 /	 \ 	 /	 \
	4	  5	6	  7
		   / \
		  /   \
		 8	   9

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

def construct_tree_helper(preorder: List[int], isLeaf: List[int], index: List[int]):
    if index[0] >= len(preorder):
        return None
    
    node = Node(data=preorder[index[0]])
    index[0] += 1
    
    if isLeaf[index[0] - 1] == 0:
        node.left = construct_tree_helper(preorder, isLeaf, index)
        node.right = construct_tree_helper(preorder, isLeaf, index)
    
    return node

def construct_binary_tree(preorder: List[int], isLeaf: List[int]):
    return construct_tree_helper(preorder, isLeaf, [0])

if __name__=="__main__":
    preorder = [1, 2, 4, 5, 3, 6, 8, 9, 7]
    isLeaf = [0, 0, 1, 1, 0, 0, 1, 1, 1]
    ans = construct_binary_tree(preorder, isLeaf)
    print_tree(ans)

