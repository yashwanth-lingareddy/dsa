'''

Given the root of a binary tree, check if the binary tree is a sum tree or not. In a sum tree, each non-leaf node's value is equal to the sum of all elements present in its left and right subtree. The value of a leaf node can be anything and the value of an empty child node is considered to be 0.

Input:

			 44
		   /	\
		  /		 \
		 9		  13
	   /   \	 /  \
	  /		\	/	 \
	 4		 5 6	  7

Output: True

Explanation: All non-leaf nodes follows the sum tree property, as shown below:

			 44 (4+5+9)+(6+7+13)
		   /	\
		  /		 \
   (4+5) 9		  13 (6+7)
	   /   \	 /  \
	  /		\	/	 \
	 4		 5 6	  7

'''

class Node:
    def __init__(self, data = None, left=None, right=None) -> None:
        self.data = data	# data field
        self.left = left	# pointer to the left child
        self.right = right	# pointer to the right child

def build_tree():
    return Node(
        data=44,
        left=Node(
            data=9,
            left=Node(data=4),
            right=Node(data=5)
        ),
        right=Node(
            data=13,
            left=Node(data=6),
            right=Node(data=7)
        )
    )

def dfs_sum(root: Node):
    if not root:
        return 0
    
    return root.data + dfs_sum(root.left) + dfs_sum(root.right)

def sum_tree(root: Node):
    if root is None:
        return True
    
    # if it is a leaf Node
    if not root.left and not root.right:
        is_sum_tree = True
    else:
        is_sum_tree = root.data == dfs_sum(root.left) + dfs_sum(root.right)
        
    return is_sum_tree and sum_tree(root.left) and sum_tree(root.right)

if __name__=="__main__":
    root = build_tree()
    ans = sum_tree(root=root)
    print(ans)