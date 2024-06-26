'''

Given the root of a binary tree, return all paths from every leaf node to the root node in the binary tree.

Input:

			 1
		   /   \
		 /		 \
		2		  3
	   / \		 / \
	  /	  \		/	\
	 4	   5   6	 7
			  / \
			 /	 \
			8	  9

Output: {(4, 2, 1), (5, 2, 1), (8, 6, 3, 1), (9, 6, 3, 1), (7, 3, 1)}

Explanation: The binary tree has five leaf-to-root paths:

4 —> 2 —> 1
5 —> 2 —> 1
8 —> 6 —> 3 —> 1
9 —> 6 —> 3 —> 1
7 —> 3 —> 1

'''
from typing import List, Set, Tuple

class Node:
    def __init__(self, data = None, left=None, right=None) -> None:
        self.data = data	# data field
        self.left = left	# pointer to the left child
        self.right = right	# pointer to the right child

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
                left=Node(data=8),
                right=Node(data=9)
            ),
            right=Node(
                data=7,
            )
        )
    )

def dfs(root: Node, path: List[int], result: Set[Tuple[int]]):
    if not root:
        return
    
    # prepend the data to the list
    path.insert(0, root.data)
    
    # if leaf node
    if not root.left and not root.right:
        result.add(tuple(path))
        
    dfs(root.left, path, result)
    dfs(root.right, path, result)
    
    # pop the first element
    path.pop(0)

def leaf_to_root_paths(root: Node):
    result = set()
    dfs(root, [], result)
    return result

if __name__=="__main__":
    root = build_tree()
    ans = leaf_to_root_paths(root)
    print(ans)