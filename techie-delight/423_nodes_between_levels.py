'''

Given the root of a binary tree and two positive numbers m and n where m >= n, return values of all nodes between level m and level n. The nodes for each level should be processed from left and right.

Input: Below binary tree, m = 2, n = 3

		   1
		 /   \
		/	  \
	   2	   3
			  / \
			 /	 \
			4	  5
		   / \	   \
		  /   \		\
		 6	   7	 8

Output: [2, 3, 4, 5]

Note: If n is more than the number of levels in the binary tree, the solution return nodes till last level. For example, if the starting level is 2 and the ending level is 7, the solution should return [2, 3, 4, 5, 6, 7, 8] for above binary tree.

'''
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
            data=2
        ),
        right=Node(
            data=3,
            left=Node(
                data=4,
                left=Node(
                    data=6
                ),
                right=Node(
                    data=7
                )
            ),
            right=Node(
                data=5,
                right=Node(
                    data=8
                )
            )
        )
    )

def nodes_between_levels(root: Node, m: int, n: int):
    nodes = []
    if not root:
        return nodes
    q = deque()
    q.append((root, 1))
    
    while len(q) > 0:
        
        for _ in range(len(q)):
            node, level = q.popleft()
            if level >= m and level <= n:
                nodes.append(node.data)
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
    
    return nodes

if __name__=="__main__":
    root = build_tree()
    m = 2
    n = 3
    ans = nodes_between_levels(root, m, n)
    print(ans)