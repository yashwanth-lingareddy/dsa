'''

Given the root of a binary tree, check if it satisfies the height-balanced property of the red–black tree or not.

The red–black tree's height-balanced property states that the path from the root to the farthest leaf is no more than twice as long as a path from the root to the nearest leaf. In other words, the maximum height of any node in a tree is not greater than twice its minimum height.

Input:
			   1
			/	 \
		   2	   3
		 /		 /   \
	   4		5	   6
			  /   \
			 7	   8
		   /   \
		  9	   10

Output: True

Input:
			   1
			/	 \
		   2	   3
		 /		 /   \
	   4		5	   6
			  /   \
			 7	   8
		   /   \
		  9		10
			  /	   \
			 11	   12

Output: False

Explanation: The tree violates the red–black tree property at node 3.

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
            data=2,
            left=Node(
                data=4
            )
        ),
        right=Node(
            data=3,
            left=Node(
                data=5,
                left=Node(
                    data=7,
                    left=Node(
                        data=9
                    ),
                    right=Node(
                        data=10
                    )
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

def min_depth(root: Node):
    if not root:
        return 0
    
    queue = deque([(root, 1)])  # (node, depth)
    
    while queue:
        node, depth = queue.popleft()
        
        # If this is a leaf node, return its depth
        if not node.left and not node.right:
            return depth
        
        # Add child nodes to the queue
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))
    
    # This line should never be reached for a non-empty tree
    return 0

def height(root: Node):
    if not root:
        return 0
    
    return 1 + max(height(root.left), height(root.right))

def is_height_balanced(root: Node):
    if not root:
        return True
    
    max_height = height(root)
    min_height = min_depth(root)
    
    is_balanced = not ((max_height) > (2 * min_height))
    
    return is_balanced and is_height_balanced(root.left) and is_height_balanced(root.right)

if __name__=="__main__":
    root = build_tree()
    ans = is_height_balanced(root)
    print(ans)