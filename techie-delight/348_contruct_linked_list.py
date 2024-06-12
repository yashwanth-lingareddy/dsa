'''

Given an array of integers, implement a linked list out of the array keys. The solution should create a new node for every key and insert it onto the list's front.

Input : [1, 2, 3, 4, 5]
Output: 1 —> 2 —> 3 —> 4 —> 5 —> None

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

if __name__ == "__main__":
    keys = [1, 2, 3, 4, 5]
    ans = construct(keys=keys)
    printed = print_linked_list(ans)
    print(printed)