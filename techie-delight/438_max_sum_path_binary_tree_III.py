'''

Given the root of a non-empty binary tree, return the maximum path sum between any two nodes in the binary tree. The path can start and end at any node in the tree and need not go through the root.

Input:

			 1
		   /   \
		 /		 \
		2		  10
	   / \		 / \
	  /	  \		/	\
	 -1	  -4   -5	 -6
		  /	  / \
		 /	 /	 \
		3	7	  4
			 \
			  \
			  -2

Output: 15

Explanation: The maximum sum path is [2, 1, 10, -5, 7].

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
            left=Node(data=-1),
            right=Node(data=-4)
        ),
        right=Node(
            data=10,
            left=Node(
                data=-5,
                left=Node(data=7, right=Node(data=-2)),
                right=Node(data=4)
            ),
            right=Node(data=-6)
        )
    )

def max_sum_util(node: Node, max_sum: List[int]):
    if not node:
        return 0
    
    # Recursively compute the maximum path sum for left and right subtrees
    left_gain = max(max_sum_util(node.left, max_sum), 0)
    right_gain = max(max_sum_util(node.right, max_sum), 0)
    
    
    # Compute the maximum path sum through the current node
    current_max_path = node.data + left_gain + right_gain
    
    # Update the global maximum sum if necessary
    max_sum[0] = max(max_sum[0], current_max_path)
    
    # Return the maximum sum of a path starting from the current node
    return node.data + max(left_gain, right_gain)

def max_sum(root: Node):
    res = [float('-inf')]
    max_sum_util(root, res)
    return res[0]

if __name__=="__main__":
    root = build_tree()
    ans = max_sum(root)
    print(ans)
