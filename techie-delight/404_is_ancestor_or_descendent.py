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

def path_to_value(root: Node, path: List[int], val: int):
    if root is None:
        return False

    path.append(root.data)

    if root.data == val or path_to_value(root.left, path, val) or path_to_value(root.right, path, val):
        return True
    path.pop()
    return False


def build_jaffa():
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

def is_ancestor_or_decendent(root: Node, v1: int, v2: int):
    p1 = []
    p2 = []
    path_to_value(tree, p1, v1)
    path_to_value(tree, p2, v2)
    search_path = p1 if len(p1) >= len(p2) else p2
    if v1 in search_path and v2 in search_path:
        return True
    return False


if __name__=="__main__":
    tree = build_tree()
    v1 = 3
    v2 = 14
    ans = is_ancestor_or_decendent(tree, v1, v2)
    print(ans)
