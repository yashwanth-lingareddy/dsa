'''

Given an integer array representing inorder sequence of a binary tree, return count of all possible binary trees having that same inorder traversal.

Input: [1, 2, 3]
Output: 5
Explanation: There are 5 binary trees with inorder traversal [1, 2, 3], as shown below:

  1			1		  2			3		   3
   \		 \		 / \	   /		  /
	2		  3		1   3	  1		  	 2
	 \		 /				   \		/
	  3		2					2	   1

'''

from typing import List

def countBinaryTrees(inorder: List[int]) -> int:
    if len(inorder) == 0:
        return 1
    
    # Write your code here...
    n = len(inorder)

    # Initialize dp array
    dp = [[0 for _ in range(n)] for _ in range(n)]
    
    # Base case: single node trees
    for i in range(n):
        dp[i][i] = 1
    
    # Fill dp table
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            for k in range(i, j + 1):
                left = dp[i][k-1] if k > i else 1
                right = dp[k+1][j] if k < j else 1
                dp[i][j] += left * right
    
    return dp[0][n-1]

if __name__=="__main__":
    inorder = [1, 2, 3]
    ans = countBinaryTrees(inorder)
    print(ans)
