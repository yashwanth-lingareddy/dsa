'''

Given the root of a binary tree, return the maximum difference between a node and its descendants in the binary tree. You may assume that the binary tree contains at-least two nodes.

Input:
		   6
		 /   \
		/	  \
	   3	   8
			  / \
			 /	 \
			2	  4
		   / \
		  /	  \
		 1	   7

Output: 7

Explanation: The maximum difference between a node and its descendants is 8 - 1 = 7.

'''

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data	# data field
        self.left = left	# pointer to the left child
        self.right = right	# pointer to the right child

def build_tree():
    return Node(
        data=6,
        left=Node(data=3),
        right=Node(
            data=8,
            left=Node(
                data=2,
                left=Node(data=1),
                right=Node(data=7)
            ),
            right=Node(data=4)
        )
    )

def dfs(root: Node, max_diff: int):
    if not root:
        return float('inf'), max_diff

    # If it is leaf node, then return the root value
    if not root.left and not root.right:
        return root.data, max_diff
    
    a, max_diff = dfs(root.left, max_diff)
    b, max_diff = dfs(root.right, max_diff)

    val = min(a, b)

    max_diff = max(max_diff, root.data - val)

    return min(val, root.data), max_diff

def find_max_diff(root: Node):
    max_diff = float('-inf')
    x, max_diff = dfs(root, float('-inf'))
    return max_diff

if __name__=="__main__":
    root = build_tree()
    ans = find_max_diff(root)
    print(ans)