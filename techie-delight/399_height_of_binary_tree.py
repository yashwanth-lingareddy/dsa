'''

Given the root of a binary tree, return the binary tree's height. The height of the binary tree is the total number of edges or nodes on the longest path from the root node to the leaf node.

The solution should consider the total number of nodes in the longest path. For example, an empty tree's height is 0, and the tree's height with only one node is 1.

Input:
		   1
		 /   \
		/	  \
	   2	   3
	  /		  / \
	 /	  	 /	 \
	4		5	  6
		   / \
		  /   \
		 7	   8

Output: 4


Input:
		   1
		 /   \
		/	  \
	   2	   3
	  /	\	  / \
	 /	 \ 	 /	 \
	4	  5	6	  7

Output: 3


Input:
		   1
		  /
		 /
		2
	   /
	  /
	 3
	/
   /
  4

Output: 4

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

def tree_height(tree: Node):
    if tree is None:
        return 0
    
    this_node_height = 1

    left_tree_height = this_node_height + tree_height(tree.left)
    right_tree_height = this_node_height + tree_height(tree.right)

    return max(left_tree_height, right_tree_height)

if __name__=="__main__":
    tree = build_tree()
    ans = tree_height(tree=tree)
    print(ans)