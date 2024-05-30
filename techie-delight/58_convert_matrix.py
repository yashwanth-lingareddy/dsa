'''

Give an `M × N` binary matrix, change all elements of row `i` and column `j` to 0 if cell (i, j) has value 0.

Input:
[
	[1, 1, 0, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 1, 0, 1],
	[1, 1, 1, 1, 1],
	[0, 1, 1, 1, 1]
]

Output:
[
	[0, 0, 0, 0, 0],
	[0, 1, 0, 0, 1],
	[0, 0, 0, 0, 0],
	[0, 1, 0, 0, 1],
	[0, 0, 0, 0, 0]
]

Explanation:

0’s are present at (0, 2), (4, 0), and (2, 3) in the input matrix. Therefore, every element of the following cells is changed to 0:

• row 0 and column 2
• row 4 and column 0
• row 2 and column 3

'''

from typing import List

def convertMatrix(mat: List[List[int]]) -> None:
    if len(mat) == 0:
        return
    # Write your code here...
    rows = set()
    columns = set()
    m = len(mat)
    n = len(mat[0])
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                rows.add(i)
                columns.add(j)
    
    # fill rows
    for i in range(m):
        if i not in rows:
            continue
        for j in range(n):
            mat[i][j] = 0
    
    # fill columns
    for j in range(n):
        if j not in columns:
            continue
        for i in range(m):
            mat[i][j] = 0
    
    return

if __name__=="__main__":
    mat = [
        [1, 1, 0, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1]
    ]
    convertMatrix(mat=mat)
    print(mat)