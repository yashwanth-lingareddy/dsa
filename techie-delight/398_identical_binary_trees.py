'''

Given the root of two binary trees, x and y, check if x is identical to y. Two binary trees are identical if they have identical structure and their contents are also the same.

Input:
		   1						1
		 /   \					  /   \
		/	  \					 /	   \
	   2	   3				2		3
	  /	\	  / \			   / \	   / \
	 /	 \ 	 /	 \			  /	  \	  /	  \
	4	  5	6	  7			 4	   5 6	   7

Output: True
Explanation: Both binary trees have the same structure and contents.

Input:
		   1						1
		 /   \					  /   \
		/	  \					 /	   \
	   2	   3				2		3
	  /	\	  / \			   / \	   /
	 /	 \ 	 /	 \			  /	  \	  /
	4	  5	6	  7			 4	   5 6

Output: False
Explanation: Both binary trees have different structures.

Input:
		   1						1
		 /   \					  /   \
		/	  \					 /	   \
	   2	   3				2		3
	  /	\	  / \			   / \	   / \
	 /	 \ 	 /	 \			  /	  \	  /	  \
	4	  5	6	  7			 4	   5 6	   8

Output: False
Explanation: Both binary trees have the same structure but differ in nodes' values.

'''

class Node:
    def __init__(self, data = None, left=None, right=None) -> None:
        self.data = data	# data field
        self.left = left	# pointer to the left child
        self.right = right	# pointer to the right child

def build_tree():
    tree = Node(
        data=1,
        left=Node(
            data=2,
            left=Node(data=4)
        ),
        right=Node(
            data=3,
            left=Node(
                data=5,
                left=Node(data=7),
                right=Node(data=8)
            ),
            right=Node(data=6)
        )
    )
    return tree

def is_identical(x: Node, y: Node):
    # if both the nodes are None, they are identical
    if x is None and y is None:
        return True
    
    # if any one is not none and the other one is none, they are not identical
    if x is None or y is None:
        return False
    
    is_this_node_identical = False

    if x.data == y.data:
        is_this_node_identical = True

    return is_this_node_identical and is_identical(x.left, y.left) and is_identical(x.right, y.right)

if __name__=="__main__":
    x = build_tree()
    y = build_tree()
    ans = is_identical(x, y)
    print(ans)