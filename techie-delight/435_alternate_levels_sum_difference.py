'''

Given the root of a binary tree, return the difference between the sum of all nodes present at odd levels and the sum of all nodes present at even level.

Input:
		   1
		 /   \
		/	  \
	   2	   3
	  /		  / \
	 /	  	 /	 \
	4	  	5	  6
		   / \
		  /	  \
		 7	   8

Output: -4

Explanation: The difference is (1 + 4 + 5 + 6) - (2 + 3 + 7 + 8) = -4

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

def is_even(val: int):
    return val % 2 == 0

def alternate_levels_sum_difference(root: Node):
    odd_sum = 0
    even_sum = 0
    
    if not root:
        return 0
    
    q = deque()
    q.append((root, 1))
    
    while len(q) > 0:
        
        for _ in range(len(q)):
            node, level = q.popleft()
            if is_even(level):
                even_sum += node.data
            else:
                odd_sum += node.data
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
    
    return odd_sum - even_sum

if __name__=="__main__":
    root = build_tree()
    ans = alternate_levels_sum_difference(root)
    print(ans)
