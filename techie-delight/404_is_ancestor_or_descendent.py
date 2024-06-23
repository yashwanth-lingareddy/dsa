'''

Given the root of a binary tree and two tree nodes, x and y, check if they lie on the same root-to-leaf path in the binary tree. In other words, determine whether x is an ancestor of y or x is a descendant of y.

For example, consider the following binary tree.

					 1
				   /   \
				 /		 \
				2		  3
			  /  \		 /  \
			 /	  \		/	 \
			4	   5   6	  7
		  /   \		\		 /
		 /	   \	 \		/
		8		9	 10	   11
			  /   \		  /
			 /	   \	 /
			12	   13	14

Input: x = Node 3, y = Node 14
Output: True
Explanation: Node 3 is an ancestor of Node 14

Input: x = Node 12, y = Node 2
Output: True
Explanation: Node 12 is a direct descendant of Node 2

Input: x = Node 4, y = Node 5
Output: False
Explanation: Node 4 is a neither an ancestor nor a descendant of Node 5

Note: The solution should return False if either x or y is not the actual node in the tree.

**: This solution doesn't pass all the test cases. Have to revisit one more time

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
            left=Node(
                data=4,
                left=Node(
                    data=8
                ),
                right=Node(
                    data=9,
                    left=Node(
                        data=12
                    ),
                    right=Node(
                        data=13
                    )
                )
            ),
            right=Node(
                data=5,
                right=Node(
                    data=10
                )
            )
        ),
        right=Node(
            data=3,
            left=Node(
                data=6,
                right=Node(
                    data=7,
                    left=Node(
                        data=11,
                        left=Node(
                            data=14
                        )
                    )
                )
            )
        )
    )
    return tree

def build_x():
    return Node(
        data=3,
        left=Node(
            data=6,
            right=Node(
                data=7,
                left=Node(
                    data=11,
                    left=Node(
                        data=14
                    )
                )
            )
        )
    )

def build_y():
    return Node(
        data=14
    )

def is_identical(x: Node, y: Node):
    if x is None and y is None:
        return True
    
    if x is None or y is None:
        return False
    
    identical = False

    if x.data == y.data:
        identical = True

    return identical and is_identical(x.left, y.left) and is_identical(x.right, y.right)


def find_path(root: Node, node: Node, path: List[int]):
    if not root:
        return False
    
    path.append(root)
    
    if is_identical(root, node):
        return True
    
    # Use below lines instead of "is_identical" to get it worked in techiedelight complier
    # if root == node:
    #     return True 
    
    if find_path(root.left, node, path) or find_path(root.right, node, path):
        return True
    
    path.pop()
    return False


def is_ancestor_or_decendent(root: Node, x: Node, y: Node):
    # base
    if not root or not x or not y:
        return False
    
    # if x and y are same, they are neither accestor or descendents to each other
    if x == y:
        return False

    path_x = []
    path_y = []

    find_path(root, x, path_x)
    find_path(root, y, path_y)

    if len(path_x) == 0 or len(path_y) == 0:
        return False
    
    # they both might have exact same path
    if len(path_x) == len(path_y):
        return False
    
    # check if they have common path until the min length
    for i in range(min(len(path_x), len(path_y))):
        if not is_identical(path_x[i], path_y[i]):
            return False
        # Use below lines instead of "is_identical" to get it worked in techiedelight complier
        # if path_x[i] != path_y[i]:
        #     return False
    
    return True

if __name__=="__main__":
    root = build_tree()
    x = build_x()
    y = build_y()
    ans = is_ancestor_or_decendent(root, x, y)
    print(ans)
