'''

Given two integer arrays representing inorder and postorder traversal of a binary tree, return the preorder traversal of the corresponding binary tree.

Input:

inorder[]   = [4, 2, 1, 7, 5, 8, 3, 6]
postorder[] = [4, 2, 7, 8, 5, 6, 3, 1]

Output: [1, 2, 4, 3, 5, 7, 8, 6]

Explanation: The inorder and postorder traversal represents the following binary tree.

		   1
		 /   \
		/	  \
	   2	   3
	  /		  / \
	 /	  	 /	 \
	4		5	  6
		   / \
		  /   \
		 7	   8

'''

from typing import List, Dict

def preorder(in_start: int, in_end: int, post_start: int, post_end: int, inorder_map: Dict[int, int], inorder: List[int], postorder: List[int]):
    if in_start > in_end:
        return []

    root = postorder[post_end]
    root_index = inorder_map[root]
    left_size = root_index - in_start

    result = [root]
    result += preorder(in_start, root_index - 1, post_start, post_start + left_size - 1, inorder_map, inorder, postorder)
    result += preorder(root_index + 1, in_end, post_start + left_size, post_end - 1, inorder_map, inorder, postorder)

    return result

def findPreorder(inorder: List[int], postorder: List[int]) -> List[int]:
    inorder_map = {val: idx for idx, val in enumerate(inorder)}
    return preorder(0, len(inorder) - 1, 0, len(postorder) - 1, inorder_map, inorder, postorder)

if __name__=="__main__":
    inorder = [4, 2, 1, 7, 5, 8, 3, 6]
    postorder = [4, 2, 7, 8, 5, 6, 3, 1]
    ans = findPreorder(inorder, postorder)
    print(ans)