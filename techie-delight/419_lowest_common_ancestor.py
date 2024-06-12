'''

Given the root of a binary tree and two tree nodes, x and y, return the lowest common ancestor (LCA) of x and y in the binary tree.

The lowest common ancestor (LCA) of two nodes x and y in a binary tree is the lowest (i.e., deepest) node that has both x and y as descendants, where each node can be a descendant of itself (so if x is reachable from w, w is the LCA). In other words, the LCA of x and y is the shared ancestor of x and y that is located farthest from the root.

For example, consider the following binary tree.

		   1
		 /   \
		/	  \
	   2	   3
	   \	  / \
		\	 /	 \
		 4	5	  6
		   / \
		  /   \
		 7	   8

Input: x = Node 6, y = Node 7
Output: Node 3
Explanation: The common ancestors of nodes 6 and 7 are 1 and 3. Out of nodes 1 and 3, the LCA is 3 as it is farthest from the root.

Input: x = Node 5, y = Node 8
Output: Node 5
Explanation: Node 8 itself is descendant of node 5 (and node 5 can be a descendant of itself).

Input: x = Node 2, y = Node 5
Output: Node 1

Note: The solution should return None if either x or y is not the actual node in the tree.

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
                ),
                right=Node(
                    data=8
                )
            ),
            right=Node(
                data=6
            )
        )
    )

def dfs(root: Node, target: int, path: List[Node]):
    if root is None:
        return False
    path.append(root)
    if root.data == target or dfs(root.left, target, path) or dfs(root.right, target, path):
        return True
    path.pop()
    return False

def pre_order_traversal(root: Node, target: Node, path: List[int]):
    if root is None:
        return
    
    path.append(root.data)
    pre_order_traversal(root.left, target, path)
    pre_order_traversal(root.right, target, path)

def find_LCA(root: Node, x: Node, y: Node):
    pathx = []
    pathy = []
    dfs(root, x.data, pathx)
    dfs(root, y.data, pathy)
    print([i.data for i in pathx])
    print([i.data for i in pathy])
    if len(pathx) == 0 or len(pathy) == 0:
        return None
    
    i = 0

    while i < min(len(pathx), len(pathy)):
        if pathx[i].data != pathy[i].data:
            break
        i += 1
    
    if i > 0:
        return pathx[i - 1]
    return None

if __name__=="__main__":
    tree = build_tree()
    x = Node(data=6)
    y = Node(data=7)
    node = find_LCA(tree, x, y)

    print(node.data)