'''

Given the root of a binary tree, return the maximum sum path from the root node to any leaf node in the binary tree.

Input:
				1
			  /   \
			/		\
		  /			  \
		 2			   3
	   /   \		 /   \
	  /		\		/	  \
	 8		 4	   5	   6
			/	  / \		\
		   /	 /   \		 \
		 10		7	  9		  5

Output: [1, 3, 5, 9]


In case multiple paths exists with the maximum sum, the solution can return any one of them.

Input:

			  -1
			/	 \
		  /		   \
		 2		   -3
	   /   \		 \
	  /		\		  \
	 4		-5		  -6
	  \				  /
	   \			 /
	   -7			8

Output: [-1, 2, 4, -7] or [-1, -3, -6, 8]

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
                data=8
            ),
            right=Node(
                data=4,
                left=Node(
                    data=10
                )
            )
        ),
        right=Node(
            data=3,
            left=Node(
                data=5,
                left=Node(data=7),
                right=Node(data=9)
            ),
            right=Node(
                data=6,
                right=Node(data=5)
            )
        )
    )

def max_sum_path(root: Node):
    if not root:
        return []

    max_sum = float('-inf')
    max_path = []

    def dfs(node: Node, current_path: List[int], current_sum: int):
        nonlocal max_sum, max_path

        if not node:
            return

        current_path.append(node.data)
        current_sum += node.data

        # If it's a leaf node, update max_sum and max_path if necessary
        if not node.left and not node.right:
            if current_sum > max_sum:
                max_sum = current_sum
                max_path = current_path.copy()

        # Explore left and right subtrees
        dfs(node.left, current_path, current_sum)
        dfs(node.right, current_path, current_sum)

        # Backtrack
        current_path.pop()

    dfs(root, [], 0)
    return max_path

if __name__=="__main__":
    root = build_tree()
    ans = max_sum_path(root)
    print(ans)
    