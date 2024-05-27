'''

Given the root of a binary tree, return the bottom view of its nodes' values. Assume the left and right child of a node makes a 45–degree angle with the parent.

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

Output: [7, 5, 8, 6]

Input:

	  1
	/   \
   /	 \
  2		  3
   \
	\
	 4
	  \
	   \
		5

Output: [2, 4, 5]

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
        left= Node(
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

def find_bottom_view(root: Node) -> List[int]:
    if not root:
        return []

    queue = deque([(root, 0)])  # (node, horizontal_distance)
    view = {}

    while queue:
        node, hd = queue.popleft()

        # Update the view with the last node at this horizontal distance
        view[hd] = node.data

        # Enqueue the left child with a smaller horizontal distance
        if node.left:
            queue.append((node.left, hd - 1))

        # Enqueue the right child with a larger horizontal distance
        if node.right:
            queue.append((node.right, hd + 1))

    # Sort the view by the horizontal distance and return the values
    return [view[hd] for hd in sorted(view)]


if __name__=="__main__":
    tree = build_tree()
    ans = find_bottom_view(tree)
    print(ans)
