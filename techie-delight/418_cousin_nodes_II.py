'''

Given the root of a binary tree and a tree node x, return values of all cousin nodes of x in the binary tree. Two nodes of a binary tree are cousins of each other only if they have different parents, but they are at the same level.

For example, consider the following binary tree.

			 1
		   /   \
		 /		 \
		2		  3
	  /  \		 /  \
	 /	  \		/	 \
	4	   5   6	  7

Input: x = Node 6
Output: [4, 5]

Input: x = Node 2
Output: []

Input: x = Node 4
Output: [6, 7]

Note: The solution should return an empty list if x is not the actual node in the tree.

'''

from typing import List
from collections import deque

class Node:
    def __init__(self, data = None, left=None, right=None) -> None:
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
            ),
            right=Node(
                data=5
            )
        ),
        right=Node(
            data=3,
            left=Node(
                data=6
            ),
            right=Node(
                data=7
            )
        )
    )

def is_identical(x: Node, y: Node):
    # if both the nodes are None, they are identical
    if x is None and y is None:
        return True
    
    # if any one is not none and the other one is none, they are not identical
    if x is None or y is None:
        return False
    
    is_this_node_identical = False

    if x.data == y.data:
        is_this_node_identical = True

    return is_this_node_identical and is_identical(x.left, y.left) and is_identical(x.right, y.right)

def find_cousin_nodes(root: Node, x: Node):
    if not root:
        return []
    
    q = deque()
    q.append((root, None))
    
    while len(q) > 0:
        this_level = []
        in_this_level = False
        parent_of_x = None
        
        for _ in range(len(q)):
            node, parent = q.popleft()
            this_level.append((node, parent))
            if node.left:
                q.append((node.left, node))
            if node.right:
                q.append((node.right, node))
        
        # At each level check if x is present in this level
        for n, p in this_level:
            if is_identical(n, x):
                in_this_level = True
                parent_of_x = p
            
            # Use below lines instead of "is_identical" to work in techiedelight complier
            # if n == x:
            #     in_this_level = True
            #     parent_of_x = p
        
        cousins = []
        # If x is present in this level,
        # All the nodes which doesn't have same parent as x are cousins
        if in_this_level and parent_of_x:
            for n, p in this_level:
                
                if not is_identical(p, parent_of_x):
                    cousins.append(n.data)
                
                # Use below lines instead of "is_identical" to work in techiedelight complier
                # if p != parent_of_x:
                #     cousins.append(n.data)
            return cousins
        
    return []

if __name__=="__main__":
    root = build_tree()
    x = Node(data=6)
    ans = find_cousin_nodes(root, x)
    print(ans)
