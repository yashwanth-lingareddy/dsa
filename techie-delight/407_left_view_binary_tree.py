'''

Given the root of a binary tree, return the left view of its nodes' values. Assume the left and right child of a node makes a 45–degree angle with the parent.

Input:
		   1
		 /	 \
		/	  \
	   2	   3
	  		 /   \
	 	  	/	  \
		   5	   6
		 /   \
		/	  \
	   7	   8

Output: [1, 2, 5, 7]

Input:

	  1
	/   \
   /	 \
  2		  3
   \	 /
	\   /
	 4 5

Output: [1, 2, 4]

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
            data=2
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

def find_left_view(root: Node):
    ans = []
    if not root:
        return ans

    queue = deque([root])

    while queue:
        level_size = len(queue)
        ans.append(queue[0].data)  # Append the leftmost node at this level
        
        for _ in range(level_size):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return ans

if __name__=="__main__":
    tree = build_tree()
    ans = find_left_view(tree)
    print(ans)

