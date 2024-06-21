'''

Given an integer array representing inorder traversal of a binary tree, construct and return a Cartesian tree from it. A Cartesian tree is a binary tree with the heap property: the parent of any node has a smaller value than the node itself.

Input: [9, 3, 7, 1, 8, 12, 10, 20, 15, 18, 5]

Output: Root of below Cartesian tree

		   1
		 /	 \
	   /	  \
	  /		   \
	 3			5
	/ \		   /
   /   \	  /
  9		7	 8
			  \
			   \
				10
			   /  \
			  /	   \
			 12	   15
				   / \
				  /   \
				 20	  18

Explanation: Refer below diagram

https://techiedelight.com/practice/images/Cartesian-Tree.png

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

def construct_cartesian_tree(inorder: List[int]):
    if not inorder:
        return None
	    
    stack: List[Node] = []
    root = None
    
    for num in inorder:
        last_popped = None
        while stack and stack[-1].data > num:
            last_popped = stack.pop()
        
        node = Node(num)
        if last_popped:
            node.left = last_popped
        
        if stack:
            stack[-1].right = node
        else:
            root = node
        
        stack.append(node)
    
    return root

if __name__=="__main__":
    inorder = [9, 3, 7, 1, 8, 12, 10, 20, 15, 18, 5]
    ans = construct_cartesian_tree(inorder=inorder)
    print(print_tree(ans, 0))