'''

Given the root of a binary tree and two tree nodes, x and y, check if x and y are cousins of each other. Two nodes of a binary tree are cousins of each other if they have different parents, but they are at the same level.

For example, consider the following binary tree.

			 1
		   /   \
		 /		 \
		2		  3
	  /  \		 /  \
	 /	  \		/	 \
	4	   5   6	  7


Input: x = Node 4, y = Node 6
Output: True

Input: x = Node 5, y = Node 6
Output: True

Input: x = Node 2, y = Node 3
Output: False

Input: x = Node 4, y = Node 3
Output: False

Note: The solution should return False if either x or y is not the actual node in the tree.

'''

from typing import List

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


def root_to_node_path(root: Node, node: Node, path: List[Node]):
    if not root:
        return False
        
    path.append(root)
    
    if is_identical(root, node):
        return True

    # Use the below lines to compile in techiedelight
    # if root == node:
    #     return True
    
    if root_to_node_path(root.left, node, path) or root_to_node_path(root.right, node, path):
        return True
    
    path.pop()
    return False

def are_cousins(root: Node, x: Node, y: Node):
    if not root:
        return False
    
    if x == y:
        return False
    
    path_x = []
    path_y = []
    
    root_to_node_path(root, x, path_x)
    root_to_node_path(root, y, path_y)
    
    if len(path_x) == 0 or len(path_y) == 0:
        return False
    
    # should be at the same level and have different parent
    if len(path_x) == len(path_y) and  not is_identical(path_x[len(path_x) - 2], path_y[len(path_y) - 2]):
        return True
    
    # Use the below lines to compile in techiedelight
    # if len(path_x) == len(path_y) and path_x[len(path_x) - 2] != path_y[len(path_y) - 2]:
    #     return True
    
    
            
    return False

if __name__=="__main__":
    root = build_tree()
    x = Node(data=4)
    y = Node(data=6)
    ans = are_cousins(root, x, y)
    print(ans)