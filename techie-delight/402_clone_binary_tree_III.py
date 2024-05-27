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

def clone_tree(tree: Node):
    if tree is None:
        return
    clone = Node(data=tree.data)
    if tree.left is not None:
        clone.left = clone_tree(tree.left)
    if tree.right is not None:
        clone.right = clone_tree(tree.right)
    return clone

def is_identical(x: Node, y: Node):
    if x is None and y is None:
        return True
    
    if x is None or y is None:
        return False
    
    identical = False

    if x.data == y.data:
        identical = True

    return identical and is_identical(x.left, y.left) and is_identical(x.right, y.right)

if __name__=="__main__":
    tree = build_tree()
    cloned_tree = clone_tree(tree)
    identical = is_identical(tree, cloned_tree)
    print(identical)

