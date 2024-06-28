'''

Given the root of a binary tree, convert it into a Left–child right–sibling (LC–RS) binary tree.

Each node in the LC–RS binary tree has two pointers: one to the node's left child and one to its next sibling in the original binary tree. So starting with the root, each node's leftmost child in the original tree is made its left child in the LC–RS binary tree, and its nearest sibling to the right in the original tree is made its right child in the binary tree.

Input:

			 1
		   /   \
		 /		 \
		2		  3
	  /  \		 /
	 /	  \		/
	4	   5   6
			  / \
			 /	 \
			7	  8

Output:

			1
		  /
		/
	   2
	 /   \
   /	   \
  4			3
   \	   /
	\	  /
	 5   6
		/
	   /
	  7
	   \
		\
		 8

Explanation:

Rewrite the binary tree shown by putting the left child node to one level below its parents and by placing the sibling next to the left child at the same level.

			 1
		   /
		 /
		2 ------- 3
	  /  \
	 /	  \
	4 ---- 5 -- 6
			   /
			  /
			 7 --- 8

Then transform this tree into a LC-RS binary tree by turning each sibling 45° clockwise.

'''

class Node:
    def __init__(self, data = None, left=None, right=None) -> None:
        self.data = data	# data field
        self.left = left	# pointer to the left child
        self.right = right	# pointer to the right child

def print_tree(root: Node, level: int = 0):
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
                data=6,
                left=Node(
                    data=7
                ),
                right=Node(
                    data=8
                )
            )
        )
    )

def convert_to_lcrs_tree(root: Node):
    if not root:
        return
    
    convert_to_lcrs_tree(root.left)
    convert_to_lcrs_tree(root.right)

    # copy right subtree
    right_subtree = root.right

    # Delete right subtree
    root.right = None

    # If root has left node
    if root.left:
        root.left.right = right_subtree
    # If root does not have left subtree
    else:
        root.left = right_subtree
    
    return

if __name__=="__main__":
    root = build_tree()
    convert_to_lcrs_tree(root)
    print_tree(root)
