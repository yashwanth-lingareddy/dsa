'''

Given the root of a binary tree, convert the binary tree into its mirror.

Input:
		   1
		 /   \
		/	  \
	   2	   3
	  / \	  / \
	 /	 \	 /	 \
	4	  5	6	  7

Output:

		   1
		 /   \
		/	  \
	   3	   2
	  / \	  / \
	 /	 \	 /	 \
	7	  6	5	  4

Explanation:
						|
						|
		   1			|		   1
		 /   \			|		 /   \
		/	  \			|		/	  \
	   2	   3		|	   3	   2
	  / \	  / \		|	  / \	  / \
	 /	 \	 /	 \		|	 /	 \	 /	 \
	4	  5	6	  7		|	7	  6	5	  4
						|
						|
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

def convert_to_mirror(root: Node) -> None:
    # Write your code here...
    if root is None:
        return
    
    # Swap the left and right children
    root.left, root.right = root.right, root.left
    
    # Recursively mirror the left and right subtrees
    convert_to_mirror(root.left)
    convert_to_mirror(root.right)

    return

if __name__=="__main__":
    root = build_tree()
    convert_to_mirror(root)
    print_tree(root)
