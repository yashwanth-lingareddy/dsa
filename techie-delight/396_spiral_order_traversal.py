'''

Given the root of a binary tree, return the spiral level order traversal of its nodes' values. The solution should consider the binary tree nodes level by level in spiral order, i.e., all nodes present at level 1 should be processed first from left to right, followed by nodes of level 2 from right to left, followed by nodes of level 3 from left to right and so on… In other words, odd levels should be processed from left to right, and even levels should be processed from right to left.

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

Output: [1, 3, 2, 4, 5, 6, 8, 7]

'''

from collections import deque

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

def spiral_order_traversal(root: Node):
    ans = []
    if not root:
        return ans
    queue = deque([root])
    left_to_right = True

    while len(queue) > 0:
        
        queue_length = len(queue)

        for i in range(queue_length):
            if left_to_right:
                # pop first item from the list
                node = queue.popleft()
                ans.append(node.data)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            else:
                # pop last item from the list
                node = queue.pop()
                ans.append(node.data)
                if node.right is not None:
                    queue.appendleft(node.right)
                if node.left is not None:
                    queue.appendleft(node.left)
            
        left_to_right = not left_to_right
    return ans

if __name__=="__main__":
    tree = build_tree()
    ans = spiral_order_traversal(tree)
    print(ans)