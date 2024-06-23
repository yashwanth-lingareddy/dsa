'''

Given the root of a binary tree with leaf nodes forming a circular doubly linked list, return the binary tree's height. Note that the leaf node's left and right pointers will act as a previous and next pointer of the circular doubly linked list, respectively.

The height of the binary tree is the total number of edges or nodes on the longest path from the root node to the leaf node. The solution should consider the total number of nodes in the longest path. For example, an empty tree's height is 0, and the tree's height with only one node is 1.

Input: Below binary tree (The leaf nodes [7, 5, 6] are connected using the left and right pointers and forming a circular doubly linked list)

		   1
		 /   \
		/	  \
	   2	   3
	  /	\		\
	 /	 \ 	 	 \
	4	  5		  6
   /
  /
 7

Output: 4

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
                data=4,
                left=Node(
                    data=7
                )
            ),
            right=Node(
                data=5
            )
        ),
        right=Node(
            data=3,
            right=Node(
                data=6
            )
        )
    )

def is_leaf_node(node: Node):
    return (node.left and node.left.right == node and node.right and node.right.left == node)

def height_of_binary_tree(root: Node):
    if not root:
        return 0
    
    if is_leaf_node(root):
        return 1
    
    return 1 + max(height_of_binary_tree(root.left), height_of_binary_tree(root.right))

if __name__=="__main__":
    root = build_tree()
    ans = height_of_binary_tree(root)
    print(ans)
