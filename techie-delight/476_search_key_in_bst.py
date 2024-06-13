'''

Given the root of a binary search tree (BST) and a key, search for the node with that key in the BST.

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
Output: True

Input: key = 5
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

def search(root: Node, key: int) -> bool:
    if root is None:
        return False
    
    if root.data == key:
        return True
    
    if key <= root.data:
        return search(root.left, key)
    else:
        return search(root.right, key)
    
if __name__=="__main__":
    root = build_tree()
    key = 25
    ans = search(root, key)
    print(ans)