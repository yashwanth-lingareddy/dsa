'''

Given the root of a binary search tree (BST) and a tree node x, find the inorder successor of x in the BST. An inorder successor of a tree node is the next node in the inorder traversal of the tree.

For example, consider the following tree:

		  15
		/	 \
	   /	  \
	  /		   \
	 10		   20
	/  \	  /  \
   /	\	 /	  \
  8		12	16	  25

Input: Node 10
Output: Node 12

Input: Node 12
Output: Node 15

• If the node does not lie in the BST, return the next greater node (if any) present in the BST.

Input: Node 5
Output: Node 8

• If the node does not lie in the BST and the next greater node also does not exist, the solution should return None.

Input: Node 30
Output: None

'''

from typing import List, Union

class Node:
    def __init__(self, data = None, left=None, right=None) -> None:
        self.data = data	# data field
        self.left = left	# pointer to the left child
        self.right = right	# pointer to the right child

def build_tree():
    return Node(
        data=15,
        left=Node(
            data=10,
            left=Node(
                data=8
            ),
            right=Node(
                data=12
            )
        ),
        right=Node(
            data=20,
            left=Node(
                data=16
            ),
            right=Node(
                data=25
            )
        )
    )

def print_tree(root: Node, level: int):
    if root is None:
        return
    print_tree(root.right, level + 1)
    print('\t' * level + '|--' + str(root.data))
    print_tree(root.left, level + 1)

def in_order_traversal(root: Node, path: List[Node]):
    if root is None:
        return
    
    in_order_traversal(root.left, path)
    path.append(root)
    in_order_traversal(root.right, path)

def in_order_successor(root: Node, x: Node) -> Union[Node, None]:
    path = []
    in_order_traversal(root, path)

    for i in range(len(path)):
        n = path[i]
        if n.data == x.data:
            j = i + 1
            if j >=0 and j < len(path):
                return path[j]
            else:
                return None
    
    for i in range(len(path)):
        n = path[i]
        if n.data > x.data:
            return n

    return None

if __name__=="__main__":
    root = build_tree()
    x = Node(data=12)
    ans = in_order_successor(root, x)
    print_tree(ans, 0)
