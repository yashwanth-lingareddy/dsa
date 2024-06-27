'''

Given the root of a binary tree, return the maximum sum of a path between any two leaves in the binary tree. You may assume that the binary tree is not skewed and contains at-least two nodes.

Input:

		  1
		/   \
	   /	 \
	  2		  3
	   \	 / \
	   -4   5   6
		   / \
		  7   8

Output: 22

Explanation: The maximum sum path between two leaves is [8, 5, 3, 6].

'''

from typing import List
class Node:
    def __init__(self, data = None, left=None, right=None) -> None:
        self.data = data	# data field
        self.left = left	# pointer to the left child
        self.right = right	# pointer to the right child

def build_tree():
    return Node(
        data=1,
        left=Node(data=2, right=Node(data=-4)),
        right=Node(
            data=3,
            left=Node(data=5, left=Node(data=7), right=Node(data=8)),
            right=Node(data=6)
        )
    )

def maxPathSumUtil(root: Node, res: List[int]):
 
    # Base Case
    if root is None:
        return 0
    
    # if root is leaf node we can return root.data
    if not root.left and not root.right:
        return root.data
    
    # Find maximumsum in left and right subtree. Also
    # find maximum root to leaf sums in left and right
    # subtrees ans store them in ls and rs
    ls = maxPathSumUtil(root.left, res)
    rs = maxPathSumUtil(root.right, res)
    
    # If both left and right children exist
    if root.left is not None and root.right is not None:
    
        # update result if needed
        res[0] = max(res[0], ls + rs + root.data)
    
        # Return maximum possible value for root being
        # on one side
        return max(ls, rs) + root.data
    
    # If any of the two children is empty, return
    # root sum for root being on one side
    if root.left is None:
        return rs + root.data
    else:
        return ls + root.data

def findMaximumSum(root: Node) -> int:
    # Write your code here...
    res = [float('-inf')]
    res1 = maxPathSumUtil(root, res)
    # we have to check if root.left is None or root.right is None
    # for ex:-   10
    #            /  \
    #         None  -5
    # this will return INT_MIN but answer is 5 which is res1
    if root.left and root.right:
        return res[0]
    return max(res[0], res1)

if __name__=="__main__":
    root = build_tree()
    root_1 = Node(data=10, right=Node(data=-5))
    ans = findMaximumSum(root_1)
    print(ans)