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

def dfs(root: Node, target: int, path: List[int]):
    if root is None:
        return False
    
    path.append(root.data)
    if root.data == target or dfs(root.left, target, path) or dfs(root.right, target, path):
        return True
    path.pop()
    return False

def all_ancestors(root: Node, x: Node):
    pathx = []
    dfs(root, x.data, pathx)
    if len(pathx) == 0:
        return []
    pathx.reverse()
    
    return pathx[1:len(pathx)]

if __name__=="__main__":
    tree = build_tree()
    x = Node(data=9)
    ans = all_ancestors(tree, x)
    print(ans)