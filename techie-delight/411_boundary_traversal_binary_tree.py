'''

Given the root of a binary tree, return the boundary traversal of its nodes' values. The solution should process the boundary nodes starting from the tree's root, in an anti-clockwise direction, without any duplicates.

Input:
				1
			  /   \
			/		\
		  /			  \
		 2			   3
	   /   \		 /   \
	  /		\		/	  \
	 4		 5	   6	   7
	/ \		  \			  /
   /   \	   \		 /
  8		9	   10	   11
	   / \			  /
	  /   \			 /
	 12   13		14

Output: [1, 2, 4, 8, 12, 13, 10, 6, 14, 11, 7, 3]

'''

from typing import List

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data	# data field
        self.left = left	# pointer to the left child
        self.right = right	# pointer to the right child

def build_tree():
    return Node(
        data=1,
        left=Node(
            data=2,
            left=Node(
                data=4,
                left=Node(
                    data=8
                ),
                right=Node(
                    data=9,
                    left=Node(
                        data=12
                    ),
                    right=Node(
                        data=13
                    )
                )
            ),
            right=Node(
                data=5,
                right=Node(
                    data=10
                )
            )
        ),
        right=Node(
            data=3,
            left=Node(
                data=6
            ),
            right=Node(
                data=7,
                left=Node(
                    data=11,
                    left=Node(
                        data=14
                    )
                )
            )
        )
    )

def find_boundary_traversal(root: Node) -> List[int]:
    # Write your code here...
    if not root:
        return []
    
    result = [root.data]
    
    def leftBoundary(node):
        if not node or (not node.left and not node.right):
            return
        result.append(node.data)
        if node.left:
            leftBoundary(node.left)
        elif node.right:
            leftBoundary(node.right)
    
    def leaves(node):
        if not node:
            return
        if not node.left and not node.right:
            result.append(node.data)
            return
        leaves(node.left)
        leaves(node.right)
    
    def rightBoundary(node):
        if not node or (not node.left and not node.right):
            return
        if node.right:
            rightBoundary(node.right)
        elif node.left:
            rightBoundary(node.left)
        result.append(node.data)
    
    # Left boundary
    if root.left:
        leftBoundary(root.left)
    
    # Leaves
    if root.left or root.right:
        leaves(root.left)
        leaves(root.right)
    
    # Right boundary (reversed)
    if root.right:
        rightBoundary(root.right)
    
    return result

if __name__=="__main__":
    root = build_tree()
    ans = find_boundary_traversal(root=root)
    print(ans)
