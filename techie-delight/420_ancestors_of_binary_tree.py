'''

Given the root of a binary tree and a tree node x, return values of all ancestors of x in the binary tree. Two nodes of a binary tree are cousins of each other if they have different parents, but they are at the same level.

For example, consider the following binary tree.

			 1
		   /   \
		 /		 \
		2		  3
	  /  \		 /  \
	 /	  \		/	 \
	4	   5   6	  7
			  /		   \
			 /			\
			8			 9

Input: x = Node 9
Output: [7, 3, 1]

Input: x = Node 6
Output: [3, 1]

Input: x = Node 5
Output: [2, 1]

The returned nodes should follow the node-to-root order. The solution should return an empty list if x is not the actual node in the tree.

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
                data=4
            ),
            right=Node(
                data=5
            )
        ),
        right=Node(
            data=3,
            left=Node(
                data=6,
                left=Node(
                    data=8
                )
            ),
            right=Node(
                data=7,
                right=Node(
                    data=9
                )
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


def dfs(root: Node, target: Node, path: List[int]):
    if root is None:
        return False
    path.append(root)
    
    if is_identical(root, target):
        return True

    # use below lines instead of "is_identical" in techie delight compiler
    # if root == target:
    #     return True
    
    if dfs(root.left, target, path) or dfs(root.right, target, path):
        return True

    path.pop()
    return False

def all_ancestors(root: Node, x: Node):
    pathx = []

    if not root or not x:
        return pathx

    dfs(root, x, pathx)
    
    if len(pathx) == 0:
        return []
    
    pathx.reverse()
    
    return [r.data for r in pathx[1:len(pathx)]]

if __name__=="__main__":
    tree = build_tree()
    x = Node(data=9)
    ans = all_ancestors(tree, x)
    print(ans)