'''

Given a sorted list in increasing order and a single node, insert the node into its correct sorted position in the list.

Input: List = 2 —> 4 —> 6 —> 8 —> None, Node = 9
Output: 2 —> 4 —> 6 —> 8 —> 9 —> None

Input: List = 2 —> 4 —> 6 —> 8 —> None, Node = 1
Output: 1 —> 2 —> 4 —> 6 —> 8 —> None

Input: List = 1 —> 2 —> 4 —> 6 —> 8 —> 9 —> None, Node = 5
Output: 1 —> 2 —> 4 —> 5 —> 6 —> 8 —> 9 —> None


'''
from typing import List
from collections import deque

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

def insert_sorted_node(head: Node, node: Node):
    if head is None:
        return node
    if head.data >= node.data:
        node.next = head
        return node
    head.next = insert_sorted_node(head.next, node)
    return head

if __name__=="__main__":
    keys = [2, 4, 6, 8]
    linked_list = construct(keys)
    node = Node(9)
    ans = insert_sorted_node(linked_list, node)
    print(print_linked_list(ans))