'''

Given the root of a binary expression tree representing algebraic expressions, evaluate it and return its value. A binary expression tree is a binary tree, where the operators are stored in the tree's internal nodes, and the leaves contain constants.

Assume that each node of the binary expression tree has zero or two children. The supported operators are +(addition), −(subtraction), *(multiplication), ÷(division) and ^(exponentiation).

Input:

			(+)
		   /   \
		 /		 \
	   (*)		 (/)
	   / \		 / \
	  /	  \		/	\
	(-)	   5   21	 7
	/ \
   /   \
  10	5

Output: 28

Explanation: The corresponding infix notation is ((10-5)*5)+(21/7) = 28 which can be produced by traversing the expression tree in an inorder fashion.

'''

class Node:
    def __init__(self, data = None, left=None, right=None) -> None:
        self.data = data	# data field
        self.left = left	# pointer to the left child
        self.right = right	# pointer to the right child

def build_tree():
    return Node(
        data='+',
        left=Node(
            data='*',
            left=Node(
                data='-',
                left=Node(data=10),
                right=Node(data=5)
            ),
            right=Node(
                data=5
            )
        ),
        right=Node(
            data='/',
            left=Node(data=21),
            right=Node(data=7)
        )
    )

def evaluate_expression(root: Node):
    if not root:
        return 0
    
    # if it is leaf node
    if not root.left and not root.right:
        return float(root.data)
    
    # Evaluate left expr
    left_value = evaluate_expression(root.left)

    # Evaluate right expr
    right_value = evaluate_expression(root.right)

    # Apply the operator
    if root.data == '+':
        return left_value + right_value
    elif root.data == '-':
        return left_value - right_value
    elif root.data == '*':
        return left_value * right_value
    elif root.data == '/':
        return left_value / right_value
    elif root.data == '^':
        return left_value ** right_value

if __name__=="__main__":
    root = build_tree()
    ans = evaluate_expression(root)
    print(ans)
