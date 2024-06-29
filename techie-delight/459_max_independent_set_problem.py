'''

Given the root of a binary tree, return the size of the Maximum Independent Set (MIS) in it.

An independent set is a set of nodes in a binary tree, no two of which are adjacent, i.e., there is no edge connecting any two. The size of an independent set is the total number of nodes it contains. The maximum independent set problem is finding an independent set of the largest possible size for a given binary tree.

Input:
		   1
		 /   \
		/	  \
	   /	   \
	  2			3
	   \	   / \
		\	  /	  \
		 4	 5	   6
			/ \
		   /   \
		  7		8

Output: 5

Explanation: The Maximum Independent Set (MIS) is [1, 4, 6, 7, 8].

'''

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data	# data field
        self.left = left	# pointer to the left child
        self.right = right	# pointer to the right child

def build_tree():
    return Node(
        data=1,
        left=Node(
            data=2,
            right=Node(data=4)
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

def mis(node: Node):
    if not node:
        return 0, 0
    
    # Recursively compute MIS for left and right subtrees
    left_inc, left_exc = mis(node.left)
    right_inc, right_exc = mis(node.right)
    
    # MIS including current node
    inc = 1 + left_exc + right_exc
    
    # MIS excluding current node
    exc = max(left_inc, left_exc) + max(right_inc, right_exc)
    
    return inc, exc

def findMISSize(root: Node) -> int:    
    return max(mis(root))

if __name__=="__main__":
    root = build_tree()
    ans = findMISSize(root)
    print(ans)
