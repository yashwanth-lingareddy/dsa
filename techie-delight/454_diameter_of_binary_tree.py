'''

Given the root of a binary tree, return the diameter of binary tree. A binary tree diameter equals the total number of nodes on the longest path between any two leaves in it.

Input:

	   1
	 /   \
	/	  \
   2	   3
	\	  / \
	 \	 /	 \
	  4	5	  6
	   / \
	  /	  \
	 7	   8

Output: 6

Explanation: The nodes involved in binary tree's diameter are [4, 2, 1, 3, 5, 7]. Note that the diameter passes through the root node.


Input:

		1
		 \
		  \
		   2
		  / \
		 /	 \
		3	  4
	   / \	   \
	  /	  \		\
	 5	   6	 7

Output: 5

Explanation: The nodes involved in binary tree's diameter are [5, 3, 2, 4, 7]. Note that the diameter does not pass through the root node.

Note: Here diameter is longest path between any two leaf nodes

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
            right=Node(
                data=4
            )
        ),
        right=Node(
            data=3,
            left=Node(
                data=5,
                left=Node(
                    data=7
                ),
                right=Node(
                    data=8
                )
            ),
            right=Node(
                data=6
            )
        )
    )

def height_of_binary_tree(root: Node):
    if root is None:
        return 0
    return 1 + max(
        height_of_binary_tree(root.left), 
        height_of_binary_tree(root.right)
    )    

def diameter_of_binary_tree(root: Node):
    if root is None:
        return 0
    left_height = height_of_binary_tree(root.left)
    right_height = height_of_binary_tree(root.right)
    diameter = left_height + right_height + 1
    return max(
        diameter,
        diameter_of_binary_tree(root.left),
        diameter_of_binary_tree(root.right)
    )
    

if __name__=="__main__":
    root = build_tree()
    ans = diameter_of_binary_tree(root)
    print(ans)