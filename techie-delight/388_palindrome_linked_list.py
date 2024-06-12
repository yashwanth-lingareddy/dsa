'''

Given a singly-linked list of integers, determine whether the linked list is a palindrome.

Input: 1 —> 2 —> 3 —> 2 —> 1 —> None
Output: True

Input: 1 —> 2 —> 3 —> 3 —> 1 —> None
Output: False

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


def is_palindrome(head: Node):
    s1 = ""
    s2 = ""
    l = []
    while head is not None:
        l.append(head.data)
        head = head.next
    
    for n in l:
        s1 += str(n)
    
    for i in range(len(l) - 1, -1, -1):
        n = l[i]
        s2 += str(n)
			
    return s1 == s2

if __name__=="__main__":
    keys = [1, 2, 3, 2 ,1]
    head = construct(keys)
    ans = is_palindrome(head)
    print(ans)
