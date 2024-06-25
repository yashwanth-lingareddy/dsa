'''

Given the root of a binary tree, convert it into a full tree by removing half nodes i.e., nodes having one child. A full binary tree is a tree in which every node other than the leaves has two children.

Input:
			 0
		   /   \
		  /		\
		 1		 2
		/		/
	   /	   /
	  3		  4
	 /		 / \
	/		/   \
   5	   6	 7

Output:

		 0
	   /   \
	  /	 	\
	 5		 4
			/ \
		   /   \
		  6	 	7

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
        data=0,
        left=Node(
            data=1,
            left=Node(
                data=3,
                left=Node(
                    data=5
                )
            )
        ),
        right=Node(
            data=2,
            left=Node(
                data=4,
                left=Node(
                    data=6
                ),
                right=Node(
                    data=7
                )
            )
        )
    )

def truncate(root: Node):
    if not root:
        return None
    
    if root.left:
        root.left = truncate(root.left)
    if root.right:
        root.right = truncate(root.right)
    
    # If there are any half nodes
    if root.left and not root.right:
        return root.left
    if not root.left and root.right:
        return root.right
    
    return root

if __name__=="__main__":
    root = build_tree()
    ans = truncate(root)
    print_tree(ans)