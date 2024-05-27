'''

Given the root of a binary tree, return the reverse level order traversal of its nodes' values. The solution should consider the binary tree nodes level by level in bottom-up order from left to right, i.e., process all nodes of the last level first, followed by all nodes of the second last level, and so on.

Input:
		   1
		 /   \
		/	  \
	   2	   3
	  /		  / \
	 /	  	 /	 \
	4		5	  6
		   / \
		  /   \
		 7	   8

Output: [7, 8, 4, 5, 6, 2, 3, 1]

'''

class Node:
    def __init__(self, data = None, left=None, right=None) -> None:
        self.data = data	# data field
        self.left = left	# pointer to the left child
        self.right = right	# pointer to the right child

def build_tree():
    tree = Node(
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
    return tree

def reverse_level_order_traversal(root: Node):
    ans = []
    if root is None:
        return ans
    queue = [root]
    
    while len(queue) > 0:
        this_level_items = []
        queue_length = len(queue)
        
        for i in range(queue_length):
            node = queue.pop(0)
            this_level_items.append(node.data)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        ans = this_level_items + ans
    return ans


if __name__=="__main__":
    tree = build_tree()
    ans = reverse_level_order_traversal(tree)
    print(ans)