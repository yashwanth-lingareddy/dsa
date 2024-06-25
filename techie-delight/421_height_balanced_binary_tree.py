'''

Given the root of a binary tree, check if it is height-balanced or not. In a height-balanced tree, the absolute difference between the height of the left and right subtree for every node is 0 or 1.

Input:
		   1
		 /   \
		/	  \
	   2	   3
	   \	  / \
		\	 /	 \
		 4	5	  6
		   / \
		  /   \
		 7	   8

Output: True

Input:
		   1
		 /   \
		/	  \
	   2	   3
			  / \
			 /	 \
			5	  6
		   / \
		  /   \
		 7	   8

Output: False

'''

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
            right=Node(
                data=4
            )
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

def height(root: Node):
    if not root:
        return 0
    
    return 1 + max(height(root.left), height(root.right))

def is_height_balanced_tree(root: Node):
    if not root:
        return True

    abs_difference = abs(height(root.left) - height(root.right))

    is_balanced = (abs_difference == 0 or abs_difference == 1)

    return is_balanced and is_height_balanced_tree(root.left) and is_height_balanced_tree(root.right)

if __name__=="__main__":
    root = build_tree()
    ans = is_height_balanced_tree(root)
    print(ans)