'''

Given root of two binary trees, x and y, determine if x can be converted into y by doing any number of swaps of its right and left branches. Two binary trees are identical if they have identical structure and same nodes' values.

Input: Two binary trees

				6
			  /   \
			/		\
		  /			  \
		 3			   8
		/ \			  / \
	   /   \		 /   \
	  1		7		4	  2
				   / \	   \
				  /   \		\
				 7	   1	 3

				6
			  /   \
			/		\
		  /			  \
		 8			   3
		/ \			  / \
	   /   \		 /   \
	  2		4		7	  1
	 /	   / \
	/	  /	  \
   3	 1	   7

Output: True

Hint: x and y are transformable if either x == y and ((x.left == y.left and x.right == y.right) or (x.left == y.right and x.right == y.left))

'''

class Node:
    def __init__(self, data = None, left=None, right=None) -> None:
        self.data = data	# data field
        self.left = left	# pointer to the left child
        self.right = right	# pointer to the right child

def build_x():
    return Node(
        data=6,
        left=Node(
            data=3,
            left=Node(data=1),
            right=Node(data=7)
        ),
        right=Node(
            data=8,
            left=Node(
                data=4,
                left=Node(data=7),
                right=Node(data=1)
            ),
            right=Node(
                data=2,
                right=Node(data=3)
            )
        )
    )

def build_y():
    return Node(
        data=6,
        left=Node(
            data=8,
            left=Node(
                data=2,
                left=Node(data=3)
            ),
            right=Node(
                data=4,
                left=Node(data=1),
                right=Node(data=7)
            )
        ),
        right=Node(
            data=3,
            left=Node(
                data=7
            ),
            right=Node(
                data=1
            )
        )
    )

def is_transformable(x: Node, y: Node):
    # Write your code here...
    if x is None and y is None:
        return True
    
    # if any one is not none and the other one is none, they are not identical
    if x is None or y is None:
        return False
    
    is_this_node_identical = False

    if x.data == y.data:
        is_this_node_identical = True
    
    return is_this_node_identical and (
        (
            is_transformable(x.left, y.left) and is_transformable(x.right, y.right)
        )
        or
        (
            is_transformable(x.left, y.right) and is_transformable(x.right, y.left)
        )
    )

if __name__=="__main__":
    x = build_x()
    y = build_y()
    ans = is_transformable(x, y)
    print(ans)
