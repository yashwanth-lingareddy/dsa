'''

Given the root of a binary tree, return corner nodes' values for each level in it.

Input:
		   1
		 /   \
		/	  \
	   2	   3
			  / \
			 /	 \
			4	  5
		   / \	   \
		  /   \		\
		 6	   7	 8

Output: [1, 2, 3, 4, 5, 6, 8]

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
            data=2
        ),
        right=Node(
            data=3,
            left=Node(
                data=4,
                left=Node(
                    data=6
                ),
                right=Node(
                    data=7
                )
            ),
            right=Node(
                data=5,
                right=Node(
                    data=8
                )
            )
        )
    )

def get_corner_nodes(root: Node):
    corner_nodes = []
		
    if not root:
        return corner_nodes
    
    q = deque()
    q.append(root)
    
    while len(q) > 0:
        
        corner_nodes.append(q[0].data)
        if len(q) > 1:
            corner_nodes.append(q[-1].data)
        
        for _ in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    return corner_nodes

if __name__=="__main__":
    root = build_tree()
    ans = get_corner_nodes(root=root)
    print(ans)