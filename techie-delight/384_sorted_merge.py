'''

Given two sorted singly-linked lists of integers, merge them into a single list in increasing order, and return it.

Input:

X: 1 —> 3 —> 5 —> 7 —> None
Y: 2 —> 4 —> 6 —> None

Output: 1 —> 2 —> 3 —> 4 —> 5 —> 6 —> 7 —> None

'''

from typing import List


class Node:
    def __init__(self, data=None, next=None):
        self.data = data	# data field
        self.next = next	# pointer to the next node


def construct(keys: List[int]) -> Node:
    l = len(keys)
    if l == 0:
        return Node()
    
    linked_list = Node(keys[l - 1])

    for i in range(l - 2, -1, -1):
        this_node = Node(keys[i])
        this_node.next = linked_list
        linked_list = this_node

    return linked_list

def print_linked_list(linked_list: Node):
    if linked_list is None:
        return "None"
    
    return f"{linked_list.data} -> {print_linked_list(linked_list.next)}"

def sorted_merge(X: Node, Y: Node):
    if X is None:
        return Y
    if Y is None:
        return X
    
    if X.data < Y.data:
        X.next = sorted_merge(X.next, Y)
        return X
    else:
        Y.next = sorted_merge(X, Y.next)
        return Y

if __name__=="__main__":
    x = [1, 3, 5, 7]
    X = construct(x)
    y = [2, 4, 6]
    Y = construct(y)
    ans = sorted_merge(X, Y)
    print(print_linked_list(ans))