'''

Given a postfix expression, efficiently evaluate it. Assume that the postfix expression contains only single-digit numeric operands, without any whitespace.

Input: '82/"
Output: 4
Explanation: 82/ will evaluate to 4 (8/2)

Input: '138*+"
Output: 4
Explanation: 138*+ will evaluate to 25 (1+8*3)

Input: '545*+5/"
Output: 5
Explanation: 545*+5/ will evaluate to 5 ((5+4*5)/5)


Assume valid postfix expression.

'''

def eval_post_fix(s: str) -> int:
    # Write your code here...
    stack = []

    for char in s:
        if char.isdigit():
            stack.append(int(char))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()

            if char == '+':
                result = operand1 + operand2
            elif char == '-':
                result = operand1 - operand2
            elif char == '*':
                result = operand1 * operand2
            elif char == '/':
                result = operand1 // operand2

            stack.append(result)
    return stack[0]

if __name__=="__main__":
    s = "545*+5/"
    ans = eval_post_fix(s)
    print(ans)

