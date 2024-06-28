'''

Given the root of a binary tree, check if each node has exactly one child or not. In other words, check whether the binary tree is skewed or not.

Input:
		  1
		 /
		/
	   2
	  /
	 /
	3

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

def build_tree():
    return Node(
        data=1,
        left=Node(
            data=2,
            left=Node(
                data=3
            )
        )
    )

def is_skewed(root: Node):
    # Write your code here...
    if not root:
        return True
    
    # If leaf node then it is skewed
    if not root.left and not root.right:
        return True
    
    # If it has both the children, then it is not skewed
    if root.left and root.right:
        return False
    
    # If the node has exactly one child, check if the subtree is skewed
    if root.left:
        return is_skewed(root.left)
    else:
        return is_skewed(root.right)

if __name__=="__main__":
    root = build_tree()
    ans = is_skewed(root)
    print(ans)
