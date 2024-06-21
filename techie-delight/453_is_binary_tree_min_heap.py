'''

Given the root of a binary tree, check if it is a min-heap or not. In order words, the binary tree must be a complete binary tree where each node has a higher value than its parent's value.

Input:
		   2
		 /   \
		/	  \
	   3	   4
	  / \	  / \
	 /	 \	 /	 \
	5	  6	8	  10

Output: True

Input:
		   5
		 /   \
		/	  \
	   3	   8
	  / \	  / \
	 /	 \	 /	 \
	2	  4	6	  10

Output: False

Hint: The tree should be a complete tree and min heap at all nodes

'''

from collections import deque

class Node:
    def __init__(self, data = None, left=None, right=None) -> None:
        self.data = data	# data field
        self.left = left	# pointer to the left child
        self.right = right	# pointer to the right child

def build_tree():
    return Node(
        data=2,
        left=Node(
            data=3,
            left=Node(data=5),
            right=Node(data=6)
        ),
        right=Node(
            data=4,
            left=Node(data=8),
            right=Node(data=10)
        )
    )

def is_complete_tree(root: Node):
    if not root:
        return True
    
    q = deque()
    q.append(root)
    has_null = False
    
    while len(q) > 0:
        this_node = q.popleft()
        
        if not this_node:
            has_null = True
        else:
            if has_null:
                return False
            q.append(this_node.left)
            q.append(this_node.right)
    
    return True

def is_min_heap_tree(root: Node):
    if not root:
        return True
    
    if not root.left and not root.right:
        return True
    
    if root.left and root.right:
        this_min_heap = root.data <= root.left.data and root.data <= root.right.data
        return this_min_heap and is_min_heap_tree(root.left) and is_min_heap_tree(root.right)
    
    if root.left:
        return root.data < root.left.data and is_min_heap_tree(root.left)
    
    if root.right:
        return root.data < root.right.data and is_min_heap_tree(root.right)

def is_binary_tree_min_heap(root: Node):
    return is_complete_tree(root) and is_min_heap_tree(root)

if __name__=="__main__":
    root = build_tree()
    ans = is_binary_tree_min_heap(root=root)
    print(ans)
