'''

Given the root of a special binary tree with each node containing an additional random pointer, return a clone of it. The random pointer can point to any node of the binary tree or can be None.

The solution should return a new binary tree which is identical to the given binary tree in terms of its structure and contents, and it should not use the nodes of the binary tree.

Input:
			  1(6)
			/	   \
		  /			 \
		2(X)		 3(X)
	   /   \		/   \
	  /		\	   /	 \
	4(3)   5(1)  6(4)	 7(X)


Here, random pointer of:

• Node 1 points to Node 6
• Node 2 points to None
• Node 3 points to None
• Node 4 points to Node 3
• Node 5 points to Node 1
• Node 6 points to Node 4
• Node 7 points to None

Output:

			  1(6)
			/	   \
		  /			 \
		2(X)		 3(X)
	   /   \		/   \
	  /		\	   /	 \
	4(3)   5(1)  6(4)	 7(X)

'''
class Node:
    def __init__(self, data = None, left=None, right=None, random=None) -> None:
        self.data = data	# data field
        self.left = left	# pointer to the left child
        self.right = right	# pointer to the right child
        self.random = random

def build_tree():
    return Node(
        data=1,
        left=Node(
            data=2,
            left=Node(
                data=4,
                random=Node(data=3)
            ),
            right=Node(
                data=5,
                random=Node(data=1)
            )
        ),
        right=Node(
            data=3,
            left=Node(
                data=6,
                random=Node(data=4)
            ),
            right=Node(
                data=7
            )
        ),
        random=Node(
            data=6
        )
    )

def is_identical(x: Node, y: Node):
    if x is None and y is None:
        return True
    
    if x is None or y is None:
        return False
    
    identical = False

    if x.data == y.data and x.random == y.random:
        identical = True

    return identical and is_identical(x.left, y.left) and is_identical(x.right, y.right)

def clone(root: Node):
    if not root:
        return None
    
    cloned_root = Node(root.data)
    cloned_root.random = root.random

    cloned_root.left = clone(root.left)
    cloned_root.right = clone(root.right)

    return cloned_root

if __name__=="__main__":
    root = build_tree()
    cloned_root = clone(root)
    ans = is_identical(root, cloned_root)
    print(ans)