'''

Given a postfix expression, construct a binary expression tree from it and return its root. The binary expression tree is a binary tree whose leaves are operands, such as constants or variable names, and the other nodes contain operators.

Input: ab+cde+**
Output: Root of the following expression tree.

			 *
		   /   \
		 /		 \
		+		  *
	   / \		 / \
	  /	  \		/	\
	 a	   b   c	 +
					/ \
				   /   \
				  d		e

'''
class Node:
    def __init__(self, data = None, left=None, right=None) -> None:
        self.data = data	# data field
        self.left = left	# pointer to the left child
        self.right = right	# pointer to the right child

def print_tree(root: Node, level: int = 0):
    if root is None:
        return
    print_tree(root.right, level + 1)
    print('\t' * level + '|--' + str(root.data))
    print_tree(root.left, level + 1)

def construct_expression_tree(postfix: str):
    # Write your code here...
    if not postfix:
        return None
    
    stack = []
    operators = set(['+', '-', '*', '/'])
    
    for c in postfix:
        root = Node(data=c)
        
        # If c is operand
        if c not in operators:
            stack.append(root)
        # If c is operator
        else:
            # first pop is right node
            right = stack.pop()
            # second pop is left node
            left = stack.pop()
            root.left = left
            root.right = right
            stack.append(root)
            
    return stack[0]

if __name__=="__main__":
    postfix = 'ab+cde+**'
    root = construct_expression_tree(postfix)
    print_tree(root)
