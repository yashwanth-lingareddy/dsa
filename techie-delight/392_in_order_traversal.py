'''

Given the root of a binary tree, return the inorder traversal of its nodes' values.

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

Output: [4, 2, 1, 7, 5, 8, 3, 6]

'''

from typing import List

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

def inOrderTraversal(root: Node, ans: List[int]):
    if not root:
        return
    if root.data is None:
        return
    inOrderTraversal(root.left, ans)
    ans.append(root.data)
    inOrderTraversal(root.right, ans)

def findInorderTraversal(root: Node) -> List[int]:
    ans = []
    inOrderTraversal(root, ans)
    return ans

if __name__=="__main__":
    tree = build_tree()
    ans = findInorderTraversal(tree)
    print(ans)