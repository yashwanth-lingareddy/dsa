'''

Given the root of a binary tree, return the maximum number of nodes at any level in the binary tree.

Input:
		   1
		 /   \
		/	  \
	   2	   3
	  /	\	  / \
	 /	 \ 	 /	 \
	4	  5	6	  7

Output: 4

Input:
		   1
		  /
		 /
		2
	   /
	  /
	 3
	/
   /
  4

Output: 1

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
            ),
            right=Node(
                data=5
            )
        ),
        right=Node(
            data=3,
            left=Node(
                data=6
            ),
            right=Node(
                data=7
            )
        )
    )

def get_max_width(root: Node):
    max_width = 0
    if not root:
        return max_width
    
    q = deque()
    q.append(root)
    
    while len(q) > 0:
        max_width = max(max_width, len(q))
        
        for _ in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    
    return max_width 

if __name__=="__main__":
    root = build_tree()
    ans = get_max_width(root=root)
    print(ans)