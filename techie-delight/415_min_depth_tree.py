'''

Given the root of a binary tree, return the minimum depth of the binary tree. The minimum depth is the total number of nodes along the shortest path in binary tree from the root node down to the nearest leaf node.

Input:

				1
			  /   \
			/		\
		  /			  \
		 2			   3
	   /   \		 /   \
	  /		\		/	  \
	 4		 5	   6	   7
	  \		  \			  / \
	   \	   \		 /   \
		8		9		10	 11
		 \
		  \
		  12

Output: 3

Explanation: The shortest path is 1 —> 3 —> 6.

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
                data=4,
                right=Node(
                    data=8,
                    right=Node(
                        data=12
                    )
                )
            ),
            right=Node(
                data=5,
                right=Node(
                    data=9
                )
            )
        ),
        right=Node(
            data=3,
            left=Node(
                data=6
            ),
            right=Node(
                data=7,
                left=Node(
                    data=10
                ),
                right=Node(
                    data=11
                )
            )
        )
    )

def find_min_depth(root: Node):
    if not root:
        return 0
    
    q = deque()
    # append root with level
    q.append((root, 1))

    while len(q) > 0:
        node, depth = q.popleft()

        if not node.left and not node.right:
            return depth
        
        if node.left:
            q.append((node.left, depth + 1))
        if node.right:
            q.append((node.right, depth + 1))
        
    return 0

if __name__=="__main__":
    root = build_tree()
    ans = find_min_depth(root=root)
    print(ans)