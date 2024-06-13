'''

Given the root of a binary search tree (BST) and an integer k, insert k into the BST. The solution should not rearrange the existing tree nodes and insert a new node with the given key at its correct position in BST.

Input: Below BST, k = 16

		  15
		/	 \
	   /	  \
	  /		   \
	 10		   20
	/  \		 \
   /	\	 	  \
  8		12		  25

Output:

		  15
		/	 \
	   /	  \
	  /		   \
	 10		   20
	/  \	  /  \
   /	\	 /	  \
  8		12	16	  25

You may assume that the key does not exist in the BST.

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
            right=Node(
                data=25
            )
        )
    )

def insert(root: Node, k: int):
    if root is None:
        return Node(data=k)
    
    if k <= root.data:
        root.left = insert(root.left, k)
    else:
        root.right = insert(root.right, k)
    return root

if __name__=="__main__":
    root = build_tree()
    k = 16
    ans = insert(root, k)
    print_tree(ans, 0)
