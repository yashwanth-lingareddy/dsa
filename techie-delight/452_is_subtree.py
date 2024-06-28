'''

Given the root of two binary trees, x and y, determine whether y is a subtree of x. A subtree of a tree T is a tree consisting of a node in T and all of its descendants in T.

Input:
		   1						3
		 /   \					  /   \
		/	  \					 /	   \
	   2	   3				6		7
	  /	\	  / \
	 /	 \ 	 /	 \
	4	  5	6	  7

Output: True
Explanation: y is a subtree of x as y = x.right.

Input:
		   1						2
		 /   \					  /   \
		/	  \					 /	   \
	   2	   3				4		5
	  /	\	  / \			   /
	 /	 \ 	 /	 \			  /
	4	  5	6	  7			 8

Output: False

'''

class Node:
    def __init__(self, data = None, left=None, right=None) -> None:
        self.data = data	# data field
        self.left = left	# pointer to the left child
        self.right = right	# pointer to the right child

def build_x():
    return Node(
        data=1,
        left=Node(
            data=2,
            left=Node(data=4),
            right=Node(data=5)
        ),
        right=Node(
            data=3,
            left=Node(data=6),
            right=Node(data=7)
        )
    )

def build_y():
    return Node(
        data=3,
        left=Node(data=6),
        right=Node(data=7)
    )

def isAnyNode(x: Node, y: Node):
    if not x:
        return False
    
    if x.data == y.data:
        return True
    
    return isAnyNode(x.left, y) or isAnyNode(x.right, y)
	
def areIdentical(root1: Node, root2: Node):

    # Base Case
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    
    # Check fi the data of both roots is same and data of
    # left and right subtrees are also same
    return root1.data == root2.data and areIdentical(root1.left, root2.left) and areIdentical(root1.right, root2.right)


def isSubtree(x: Node, y: Node) -> bool:
    # Write your code here...
    # Base Case
    if y is None:
        return True
    
    if x is None:
        return False
    
    # is Y is a leaf node, check if any node in tree x is equal to y
    if not y.left and not y.right:
        return isAnyNode(x, y)
    
    # Check the tree with root as current node
    if (areIdentical(x, y)):
        return True
    
    # IF the tree with root as current node doesn't match
    # then try left and right subtree one by one
    return isSubtree(x.left, y) or isSubtree(x.right, y)

if __name__=="__main__":
    x = build_x()
    y = build_y()
    ans = isSubtree(x, y)
    print(ans)