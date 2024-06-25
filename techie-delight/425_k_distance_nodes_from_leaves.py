'''

Given the root of a binary tree and a positive number k, return all nodes present at distance k from any leaf node. The solution should report only those nodes that are present in the root-to-leaf path for that leaf.

For example, consider the following binary tree.

				1
			  /   \
			/		\
		  /			  \
		 2			   3
	   /   \		 /   \
	  /		\		/	  \
	 4		 5	   6	   7
				 /
				/
			   8

Input: k = 1
Output: {2, 6, 3}

Input: k = 2
Output: {1, 3}

Input: k = 3
Output: {1}

Note: If k is more than the number of levels in the binary tree, the solution return an empty set.

'''

from typing import List, Set

class Node:
    def __init__(self, data = None, left=None, right=None) -> None:
        self.data = data	# data field
        self.left = left	# pointer to the left child
        self.right = right	# pointer to the right child

def is_identical(x: Node, y: Node):
    # if both the nodes are None, they are identical
    if x is None and y is None:
        return True
    
    # if any one is not none and the other one is none, they are not identical
    if x is None or y is None:
        return False
    
    is_this_node_identical = False

    if x.data == y.data:
        is_this_node_identical = True

    return is_this_node_identical and is_identical(x.left, y.left) and is_identical(x.right, y.right)

def build_tree():
    return Node(
        data=1,
        left=Node(
            data=2,
            left=Node(data=4),
            right=Node(data=5)
        ),
        right=Node(
            data=3,
            left=Node(
                data=6,
                left=Node(data=8)
            ),
            right=Node(data=7)
        )
    )


def dfs(root: Node, path: List[Node], k: int, result: Set[Node]):
    if not root:
        return
    
    
    path.append(root)
    
    # if leaf node then return
    if not root.left and not root.right:
        print(path)
        if k < len(path):
            result.add(path[len(path) - 1 - k])
        return
    
    if root.left:
        dfs(root.left, path, k, result)
        path.pop()
    if root.right:
        dfs(root.right, path, k, result)
        path.pop()	

def find_nodes(root: Node, k: int):
    path = []
    result = set()
    dfs(root, path, k, result)
    return result

if __name__=="__main__":
    root = build_tree()
    k = 1
    ans = find_nodes(root, k)
    print([a.data for a in list(ans)])