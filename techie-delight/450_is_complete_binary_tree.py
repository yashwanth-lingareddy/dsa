'''

Given the root of a binary tree, check if it is a complete binary tree or not. A complete binary tree is a binary tree in which every level, except possibly the last, is filled, and all nodes are as far left as possible.

Input:
		   1
		 /   \
		/	  \
	   2	   3
	  / \	  /
	 /	 \	 /
	4	 5	6

Output: True

Input:
		   1
		 /   \
		/	  \
	   2	   3
	  /		  / \
	 /		 /	 \
	4		5	  6

Output: False

'''

from typing import List
from collections import deque

class Node:
    def __init__(self, data = None, left=None, right=None) -> None:
        self.data = data	# data field
        self.left = left	# pointer to the left child
        self.right = right	# pointer to the right child

def build_tree():
    tree = Node(
        data=1,
        left=Node(
            data=2,
            left=Node(
                data=4
            )
        ),
        right=Node(
            data=3,
            left=Node(data=5),
            right=Node(data=6)
        )
    )
    return tree

def is_complete_tree(root: Node):
    if not root:
        return True

    queue = deque()
    queue.append(root)
    has_null = False

    while queue:
        node = queue.popleft()
        if node is None:
            has_null = True
        else:
            if has_null:
                return False
            queue.append(node.left)
            queue.append(node.right)

    return True

if __name__=="__main__":
    tree = build_tree()
    ans = is_complete_tree(tree)
    print(ans)
