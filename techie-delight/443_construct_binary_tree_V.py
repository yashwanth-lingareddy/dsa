'''

Given two integer arrays representing preorder and postorder traversal of a binary tree, construct and return the full binary tree. A full binary tree is a tree in which every node has either 0 or 2 children.

Input:

preorder[]  = [1, 2, 4, 5, 3, 6, 8, 9, 7]
postorder[] = [4, 5, 2, 8, 9, 6, 7, 3, 1]

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

def build_tree(preorder: List[int], postorder: List[int], pre_start: int, pre_end: int, post_start: int, post_end: int):
    if len(preorder) == 0:
        return None

    if len(postorder) == 0:
        return None
    
    if pre_start > pre_end:
        return None
    
    root = Node(preorder[pre_start])
    
    if pre_start == pre_end:
        return root
    
    # Find the index of the left child in postorder
    left_child_index = postorder.index(preorder[pre_start + 1])
    left_subtree_size = left_child_index - post_start + 1
    
    # Recursively construct left and right subtrees
    root.left = build_tree(preorder, postorder, pre_start + 1, pre_start + left_subtree_size,
                            post_start, left_child_index)
    root.right = build_tree(preorder, postorder, pre_start + left_subtree_size + 1, pre_end,
                            left_child_index + 1, post_end - 1)
    
    return root

def construct_tree(preorder: List[int], postorder: List[int]):
    return build_tree(preorder, postorder, 0, len(preorder) - 1, 0, len(postorder) - 1)

if __name__=="__main__":
    preorder  = [1, 2, 4, 5, 3, 6, 8, 9, 7]
    postorder = [4, 5, 2, 8, 9, 6, 7, 3, 1]
    ans = construct_tree(preorder, postorder)
    print_tree(ans)