'''

Given the root of a binary tree, return all paths from the root node to every leaf node in the binary tree.

Input:

			 1
		   /   \
		 /		 \
		2		  3
	  /  \		 /  \
	 /	  \		/	 \
	4	   5   6	  7
			  /		   \
			 /			\
			8			 9

Output: {(1, 2, 4), (1, 2, 5), (1, 3, 6, 8), (1, 3, 7, 9)}

Explanation: The binary tree has four root-to-leaf paths:

1 —> 2 —> 4
1 —> 2 —> 5
1 —> 3 —> 6 —> 8
1 —> 3 —> 7 —> 9

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
                left=Node(data=8)
            ),
            right=Node(
                data=7,
                right=Node(data=9)
            )
        )
    )

def dfs(root: Node, path: List[int], result: Set[Tuple[int]]):
    if not root:
        return
    
    path.append(root.data)
    
    # if leaf node
    if not root.left and not root.right:
        result.add(tuple(path))
        
    dfs(root.left, path, result)
    dfs(root.right, path, result)
    path.pop()

def root_to_leaf_paths(root: Node):
    result = set()
    dfs(root, [], result)
    return result

if __name__=="__main__":
    root = build_tree()
    ans = root_to_leaf_paths(root)
    print(ans)