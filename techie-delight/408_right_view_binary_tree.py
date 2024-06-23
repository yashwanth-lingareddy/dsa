'''

Given the root of a binary tree, return the right view of its nodes' values. Assume the left and right child of a node makes a 45–degree angle with the parent.

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

Output: [1, 3, 6, 8]

Input:

	  1
	/   \
   /	 \
  2		  3
   \	 /
	\   /
	 4 5

Output: [1, 3, 5]

'''
from collections import deque

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data	# data field
        self.left = left	# pointer to the left child
        self.right = right	# pointer to the right child

def build_tree():
    return Node(
        data=1,
        left=Node(data=2),
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

def get_right_view(root: Node):
    right_view = []
    if not root:
        return right_view
    
    q = deque()
    q.append(root)

    while len(q) > 0:
        # append right most element of this level
        right_view.append(q[-1].data)

        for _ in range(len(q)):
            current_node = q.popleft()
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)
    
    return right_view

if __name__=="__main__":
    root = build_tree()
    right_view = get_right_view(root)
    print(right_view)

