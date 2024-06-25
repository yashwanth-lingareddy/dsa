'''

Given the root of a binary tree and a positive number k, remove nodes from the tree which lie on a complete path having a sum less than k. Since a node can be part of multiple paths, delete it only if all paths from it have a sum less than k.

A complete path in a binary tree is defined as a path from the root to a leaf. The sum of all nodes on that path is defined as the sum of that path.


Input: Below binary tree, k = 20

		 6
	   /   \
	  /		\
	 3		 8
		   /   \
		  /		\
		 4		 2
	   /   \	  \
	  /		\	   \
	 1		 7		3

Output:

	  6
	   \
		\
		 8
		/
	   /
	  4
	   \
		\
		 7

The deletion should be done in a bottom-up manner until the path has a root-to-leaf sum greater than or equal to `k`. For example:

Input: Below binary tree, k = 3

         1
       /   \
      /     \
     2       3
      \     / \
       \   /   \
       -4 5     6

Output:

         1
       /   \
      /     \
     2       3
            / \
           /   \
          5     6

'''

class Node:
    def __init__(self, data = None, left=None, right=None) -> None:
        self.data = data	# data field
        self.left = left	# pointer to the left child
        self.right = right	# pointer to the right child

def print_tree(root: Node, level = 0):
    if root is None:
        return
    print_tree(root.right, level + 1)
    print('\t' * level + '|--' + str(root.data))
    print_tree(root.left, level + 1)

def build_tree():
	return Node(
		data=6,
		left=Node(
			data=3
		),
		right=Node(
			data=8,
			left=Node(
				data=4,
				left=Node(data=1),
				right=Node(data=7)
			),
			right=Node(
				data=2,
				right=Node(data=3)
			)
		),	
	)

def dfs(root: Node, k: int, sum: int):
	if not root:
		return None
	
	sum += root.data
	
	if root.left:
		root.left = dfs(root.left, k, sum)
	if root.right:
		root.right = dfs(root.right, k, sum)
		
	# if it is leaf Node
	if not root.left and not root.right:
		# if sum is less than k
		if sum < k:
			return None
	
	sum -= root.data
	
	return root

def truncate(root: Node, k: int):
    return dfs(root, k, 0)

if __name__=="__main__":
	root = build_tree()
	k = 20
	ans = truncate(root, k)
	print_tree(ans)