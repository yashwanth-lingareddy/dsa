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

def dfs(root: Node, path: List[int], result: List[List[int]]):
    if not root:
        return
    
    path.append(root.data)
    
    # if leaf node
    if not root.left and not root.right:
        result.append(path[:])
        
    dfs(root.left, path, result)
    dfs(root.right, path, result)
    path.pop()

def max_sum_path(root: Node):
    result = []
    dfs(root, [], result)
    max_sum = float('-inf')
    this_r = []
    for a in result:
        this_sum = sum(a)
        if this_sum > max_sum:
            max_sum = this_sum
            this_r = a
    return this_r

if __name__=="__main__":
    root = build_tree()
    ans = max_sum_path(root)
    print(ans)
    