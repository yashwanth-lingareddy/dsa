'''

Given the root of a binary tree and two tree nodes, x and y, return the distance between x and y in the binary tree. The distance between two nodes is defined as the total number of edges in the shortest path from one node to other.

For example, consider the following binary tree.

		  1
		/   \
	   /	 \
	  2		  3
	   \	 / \
		4   5   6
		   /	 \
		  7		  8

Input: x = Node 7, y = Node 6
Output: 3

Input: x = Node 4, y = Node 8
Output: 5

Input: x = Node 5, y = Node 5
Output: 0

Note: The solution should return a negative value if either x or y is not the actual node in the tree.

'''

from typing import List

class Node:
    def __init__(self, data = None, left=None, right=None) -> None:
        self.data = data	# data field
        self.left = left	# pointer to the left child
        self.right = right	# pointer to the right child

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

def build_tree():
    return Node(
        data=1,
        left=Node(
            data=2,
            right=Node(
                data=4
            )
        ),
        right=Node(
            data=3,
            left=Node(
                data=5,
                left=Node(
                    data=7
                )
            ),
            right=Node(
                data=6,
                right=Node(
                    data=8
                )
            )
        )
    )

def get_path(root: Node, node: Node, path: List[Node]):
    if not root:
        return False
    
    path.append(root)
    
    if is_identical(root, node):
        return True

    # Use below lines instead of "is_indentical" in techiedelight compiler
    # if root == node:
    #     return True
    
    if get_path(root.left, node, path) or get_path(root.right, node, path):
        return True
    
    path.pop()
    return False

def get_distance_between_nodes(root: Node, x: Node, y: Node):
    if not root:
        return -1
    
    if x == y:
        return 0
        
    path_x = []
    path_y = []
    
    get_path(root, x, path_x)
    get_path(root, y, path_y)
    
    if len(path_x) == 0 or len(path_y) == 0:
        return -1
    
    lca_index = -1
    for i in range(min(len(path_x), len(path_y))):
        # Use below lines instead of "is_indentical" in techiedelight compiler
        # if path_x[i] == path_y[i]:
        #     lca_index = i
        if is_identical(path_x[i], path_y[i]):
            lca_index = i
        else:
            break
    
    return len(path_x[lca_index+1:]) + len(path_y[lca_index+1:])

if __name__=="__main__":
    root = build_tree()
    x = Node(data=7)
    y = Node(
        data=6,
        right=Node(data=8)
    )
    ans = get_distance_between_nodes(root, x, y)
    print(ans)