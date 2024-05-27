'''

Given an integer array representing the parent-child relationship in a binary tree, find the tree's height without building the tree. The parent-child relationship is defined by (A[i], i) for every index i in array A. The root node's value will be i if -1 is present at index i in the array.

The height of a "node" is the total number of edges on the longest path from the node to a leaf. The height of a "tree" would be the height of its root node, or equivalently, the depth of its deepest node. A leaf node will have a height of 0 and an empty tree has height −1.

Input: [-1, 0, 0, 1, 2, 2, 4, 4]
Output: 3
Explanation: The parent array represents the folllowing binary tree

		   0
		 /   \
		/	  \
	   1	   2
	  /		  / \
	 /	  	 /	 \
	3		4	  5
		   / \
		  /   \
		 6	   7

• -1 is present at index 0, which implies that the binary tree root is node 0.
• 0 is present at index 1 and 2, which implies that the left and right children of node 0 are 1 and 2.
• 1 is present at index 3, which implies that the left or the right child of node 1 is 3.
• 2 is present at index 4 and 5, which implies that the left and right children of node 2 are 4 and 5.
• 4 is present at index 6 and 7, which implies that the left and right children of node 4 are 6 and 7.

'''

from typing import List

def fill_depth(parent_arr: List[int], current_node: int, depth_arr: List[int]):
    # Depth already filled
    if depth_arr[current_node] != 0:
        return
    
    # If this is root element
    if current_node == -1:
        depth_arr[current_node] = 1
        return
    
    # if the current_node's parent depth is not filled
    if depth_arr[parent_arr[current_node]] == 0:
        fill_depth(parent_arr, parent_arr[current_node], depth_arr)
    
    depth_arr[current_node] = depth_arr[parent_arr[current_node]] + 1

def height_of_tree(parent_arr: List[int]):
    # If the array is empty
    # return 0 if height is defined as no of nodes from root to leaf
    # return -1 if height is defined as no of edges from root to leaf
    # here the defined as no of edges from root to leaf, hence returning -1
    if len(parent_arr) == 0:
        return -1
    
    depth_arr = [0 for i in range(len(parent_arr))]

    for i, p in enumerate(parent_arr):
        fill_depth(parent_arr, p, depth_arr)
    
    # The height of binary tree is maximum of all
    # depths. Find the maximum in depth[] and assign
    # it to ht
    ht = depth_arr[0]
    for i in range(1, len(parent_arr)):
        ht = max(ht, depth_arr[i])
 
    # If height is no of nodes from root to leaf then return ht
    # If height is no of edges from root to leaf then return ht - 1
    # here the height is defined as no of edges from root to leaf. Hence returning ht - 1
    return ht - 1

if __name__=="__main__":
    input = [-1, 0, 0, 1, 2, 2, 4, 4]
    ans = height_of_tree(input)
    print(ans)