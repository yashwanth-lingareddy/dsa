'''

Given the root of a binary tree, in-place replace each node's value to the sum of all elements present in its left and right subtree. You may assume the value of an empty child node to be 0.

Input:

	   1
	 /   \
	/	  \
   2	   3

Output:

	   5
	 /   \
	/	  \
   0	   0


Input:

	   1
	 /	 \
	/	  \
   /	   \
  2			3
   \	   / \
	\	  /	  \
	 4   5	   6
		/ \
	   /   \
	  7		8

Output:

	   35
	 /	  \
	/	   \
   /		\
  4			26
   \	   /  \
	\	  /	   \
	 0   15		0
		/  \
	   /	\
	  0		 0

'''
class Node:
    def __init__(self, data = None, left=None, right=None) -> None:
        self.data = data	# data field
        self.left = left	# pointer to the left child
        self.right = right	# pointer to the right child

def print_tree(root: Node, level = 0):
    if root is None:
        return
    print_tree(root.right, level + 1)
    print('\t' * level + '|--' + str(root.data))
    print_tree(root.left, level + 1)

def build_tree():
    return Node(
        data=1,
        left=Node(
            data=2,
            right=Node(
                data=4
            )
        ),
        right=Node(
            data=3,
            left=Node(
                data=5,
                left=Node(data=7),
                right=Node(data=8)
            ),
            right=Node(
                data=6
            )
        )
    )


def dfs(root: Node):
    if not root:
        return 0
    
    original_val = root.data
    
    root.data = dfs(root.left) + dfs(root.right)
		
    return root.data + original_val

def transform(root: Node) -> None:
    dfs(root=root)

if __name__=="__main__":
    root = build_tree()
    transform(root)
    print_tree(root)
