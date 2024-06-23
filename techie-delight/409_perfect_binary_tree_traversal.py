'''

Given the root of a perfect binary tree, return the values of alternating left and right nodes for each level.

Input:
					1
				  /	   \
			   /		 \
			/			   \
		  2					 3
		/   \				/  \
	  /		  \			  /		 \
	 4		   5		 6		  7
	/ \		  / \		/ \		 / \
   /   \	 /   \	   /   \	/   \
  8		9   10   11   12   13  14   15

Output: [1, 2, 3, 4, 7, 5, 6, 8, 15, 9, 14, 10, 13, 11, 12]

0, 1, 2, 3, 4, 5, 6, 7
l = 8, l - i - 1
0 = 7 = 8 - 0 - 1
1 = 6 = 8 - 1 - 1
2 = 5 = 8 - 2 - 1
3 = 4
4 = 3
5 = 2
6 = 1
7 = 0

'''
from collections import deque
from typing import List

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data	# data field
        self.left = left	# pointer to the left child
        self.right = right	# pointer to the right child

def build_tree():
    return Node(
        data=1,
        left=Node(
            data=2,
            left=Node(
                data=4,
                left=Node(
                    data=8
                ),
                right=Node(
                    data=9
                )
            ),
            right=Node(
                data=5,
                left=Node(
                    data=10
                ),
                right=Node(
                    data=11
                )
            )
        ),
        right=Node(
            data=3,
            left=Node(
                data=6,
                left=Node(
                    data=12
                ),
                right=Node(
                    data=13
                )
            ),
            right=Node(
                data=7,
                left=Node(
                    data=14
                ),
                right=Node(
                    data=15
                )
            )
        )
    )

def traverse(root: Node):
    path = []
    if root is None:
        return path
    
    q = deque()
    q.append(root)

    while len(q) > 0:
        level_size = len(q)
        temp = []

        for _ in range(level_size):
            node = q.popleft()
            temp.append(node.data)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        j = -1
        this_level_path = [0] * level_size
        for i in range(level_size):
            if 2*i < level_size:
                this_level_path[2*i] = temp[i]
            else:
                j = i
                break
        for i in range(level_size - 1, -1, -2):
            this_level_path[i] = temp[j]
            j += 1

        path += this_level_path
    
    return path

if __name__=="__main__":
    root = build_tree()
    ans = traverse(root=root)
    print(ans)