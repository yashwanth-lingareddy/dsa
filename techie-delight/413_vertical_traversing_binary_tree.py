'''

Given the root of a binary tree, return the vertical traversal of its nodes' values. In a vertical traversal, nodes of a binary tree are processed in vertical order from left to right. Assume that the left and right child makes a 45–degree angle with the parent.

Input:
		   1
		 /	 \
		/	  \
	   2	   3
	  		 /   \
	 	  	/	  \
		   5	   6
		 /   \
		/	  \
	   7	   8

Output: [2, 7, 1, 5, 3, 8, 6]

Explanation: The binary tree has four vertical levels:

[2, 7]
[1, 5]
[3, 8]
[6]

'''

from collections import deque, defaultdict

class Node:
    def __init__(self, data=None, left=None, right=None):
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
                data=5,
                left=Node(
                    data=7
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

def vertical_traversal(root: Node):
    if not root:
        return []

    # Dictionary to store nodes by their horizontal distance
    column_table = defaultdict(list)
    # Queue to perform BFS, storing nodes along with their horizontal distance
    queue = deque([(root, 0)])

    while queue:
        node, column = queue.popleft()
        column_table[column].append(node.data)
        if node.left:
            queue.append((node.left, column - 1))
        if node.right:
            queue.append((node.right, column + 1))
    
    # Extract the entries from the column table, sorted by the column index
    sorted_columns = sorted(column_table.items())
    
    # Flatten the result
    result = [val for column, values in sorted_columns for val in values]
    
    return result

if __name__=="__main__":
    root = build_tree()
    ans = vertical_traversal(root=root)
    print(ans)