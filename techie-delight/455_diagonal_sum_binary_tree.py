'''

Given the root of a binary tree, return the sum of all nodes for each diagonal having negative slope `\`. Assume that the left and right child of a node makes a 45–degree angle with the parent.

Input:
				 1
			 .		 .
		   .		   .
		 2				 3
	   .			   .	.
	 .				 .		  .
   4			   5			6
				 .   .
			   .	   .
			 7			 8

Output: [10, 15, 11]

Explanation: The binary tree has three diagonals - [1, 3, 6], [2, 5, 8], and [4, 7]. The sum of diagonals is 10, 15, and 11 respectively.

'''
from typing import List
from collections import deque

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data	# data field
        self.left = left	# pointer to the left child
        self.right = right	# pointer to the right child

def build_tree():
    return Node(
        data=1,
        left=Node(
            data=2,
            left=Node(data=4)
        ),
        right=Node(
            data=3,
            left=Node(
                data=5,
                left=Node(data=7),
                right=Node(data=8)
            ),
            right=Node(data=6)
        )
    )

def findDiagonalSum(root: Node) -> List[int]:
    # Write your code here...
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        size = len(queue)
        this_sum = 0
        for _ in range(size):
            node = queue.popleft()
            
            # Traverse right as far as possible
            while node:
                this_sum += node.data
                # result.append(node.data)
                if node.left:
                    queue.append(node.left)
                node = node.right
        result.append(this_sum)
    return result

if __name__=="__main__":
    root = build_tree()
    ans = findDiagonalSum(root)
    print(ans)
