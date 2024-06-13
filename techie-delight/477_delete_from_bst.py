'''

Given the root of a binary search tree (BST) and a key, delete the node with that key in the BST if it exists, and return the root node.

• When deleting a node with no children, the solution should remove the node from the tree.
• When deleting a node with one child, the solution should remove the node and replace it with its child.
• When deleting a node with two children, the solution should swap the node's value with either its inorder successor or inorder predecessor, and then call delete on the inorder successor or inorder predecessor. This node will have at-most one child and can be deleted according to one of the two simpler cases above.

For example, consider the following BST.

		  15
		/	 \
	   /	  \
	  /		   \
	 10		   20
	/  \	  /  \
   /	\	 /	  \
  8		12	16	  25

Input: key = 25
Output:

		  15
		/	 \
	   /	  \
	  /		   \
	 10		   20
	/  \	  /
   /	\	 /
  8		12	16

Input: key = 15
Output:

		  12					  16
		/	 \			  		/	 \
	   /	  \			 	   /	  \
	  /		   \		 or   /		   \
	 10		   20		   	 10		   20
	/		  /  \		  	/  \		 \
   /		 /	  \		   /	\	 	  \
  8			16	  25	  8		12		  25

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

def min_node(root: Node):
    if root.left is None:
        return root
    return min_node(root.left)

def delete_node(root: Node, key: int):
    if root is None:
        return None
    if key < root.data:
        root.left = delete_node(root.left, key)
    elif key > root.data:
        root.right = delete_node(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            successor = min_node(root.right)
            root.data = successor.data
            root.right = delete_node(root.right, successor.data)
    return root

if __name__=="__main__":
    root = build_tree()
    key = 25
    ans = delete_node(root, key)
    print_tree(ans, 0)
