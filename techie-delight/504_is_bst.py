'''

Given the root of a binary tree, check if it is a binary search tree (BST) or not.

Input:
		  15
		/	 \
	   /	  \
	  /		   \
	 10		   20
	/  \	  /  \
   /	\	 /	  \
  8		12	16	  25

Output: True

Input:
		   1
		 /   \
		/	  \
	   2	   3

Output: False

'''

class Node:
    def __init__(self, data = None, left=None, right=None) -> None:
        self.data = data	# data field
        self.left = left	# pointer to the left child
        self.right = right	# pointer to the right child

def print_tree(root: Node, level: int):
    if root is None:
        return
    print_tree(root.right, level + 1)
    print('\t' * level + '|--' + str(root.data))
    print_tree(root.left, level + 1)

def build_tree():
    return Node(
        data=15,
        left=Node(
            data=10,
            left=Node(
                data=8
            ),
            right=Node(
                data=12
            )
        ),
        right=Node(
            data=20,
            left=Node(
                data=16
            ),
            right=Node(
                data=25
            )
        )
    )

def is_valid_bst(root: Node, min_val = float('-inf'), max_value = float('inf')):
    if root is None:
        return True
    
    if root.data <= min_val or root.data >= max_value:
        return False
    
    return is_valid_bst(root.left, min_val, root.data) and is_valid_bst(root.right, root.data, max_value)

def is_bst(root: Node):
    return is_valid_bst(root)

if __name__=="__main__":
    root = build_tree()
    ans = is_bst(root)
    print(ans)
