'''

Given two integer arrays representing inorder and preorder traversal of a binary tree, return the postorder traversal of the corresponding binary tree.

Input:

inorder[]  = [4, 2, 1, 7, 5, 8, 3, 6]
preorder[] = [1, 2, 4, 3, 5, 7, 8, 6]

Output: [4, 2, 7, 8, 5, 6, 3, 1]

Explanation: The inorder and preorder traversal represents the following binary tree.

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

from typing import List

def findPostorder(inorder: List[int], preorder: List[int]) -> List[int]:
    # Write your code here...
    if not inorder or not preorder:
        return []

    root = preorder[0]
    root_index = inorder.index(root)

    left_inorder = inorder[:root_index]
    right_inorder = inorder[root_index + 1:]

    left_preorder = preorder[1:root_index + 1]
    right_preorder = preorder[root_index + 1:]

    left_postorder = findPostorder(left_inorder, left_preorder)
    right_postorder = findPostorder(right_inorder, right_preorder)

    return left_postorder + right_postorder + [root]

if __name__=="__main__":
    inorder = [4, 2, 1, 7, 5, 8, 3, 6]
    preorder = [1, 2, 4, 3, 5, 7, 8, 6]
    ans = findPostorder(inorder, preorder)
    print(ans)