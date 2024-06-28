'''

Given the root of a binary tree, check if the binary tree has a symmetric structure or not, i.e., left and right subtree mirror each other.

Input:
		   1
		 /   \
		/	  \
	   2	   3
		\	  /
		 \	 /
		  4	5

Output: True

Input:
		   1
		 /   \
		/	  \
	   2	   3
	  / \	  / \
	 /   \	 /	 \
	7	  8	5	  6

Output: True

Input:
		   1
		 /   \
		/	  \
	   2	   3
	  /		  /
	 /		 /
	7		5

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
            left=Node(data=7),
            right=Node(data=8)
        ),
        right=Node(
            data=3,
            left=Node(data=5),
            right=Node(data=6)
        )
    )

def is_mirror(left: Node, right: Node):
    # if it is a leaf node, then it is a mirror image
    if not left and not right:
        return True
    
    # If one node is None and the other isn't, they are not mirror images
    if not left or not right:
        return False
    
    return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)

def is_symmetric(root: Node):
    if not root:
        return True
    
    return is_mirror(root.left, root.right)

if __name__=="__main__":
    root = build_tree()
    ans = is_symmetric(root)
    print(ans)
