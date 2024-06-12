'''

Given a singly-linked list of integers, rearrange its nodes to be sorted in increasing order.

Input : 6 —> 3 —> 4 —> 8 —> 2 —> 9 —> None
Output: 2 —> 3 —> 4 —> 6 —> 8 —> 9 —> None

Input : 9 —> -3 —> 5 —> -2 —> -8 —> -6 —> None
Output: -8 —> -6 —> -3 —> -2 —> 5 —> 9 —> None

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

def merge_sort(head1: Node, head2: Node):
    if head1 is None:
        return head2
        
    if head2 is None:
        return head1
        
    if head1.data < head2.data:
        head1.next = merge_sort(head1.next, head2)
        return head1
    head2.next = merge_sort(head1, head2.next)
    return head2

def get_mid(head: Node):
    if head is None:
        return head
    
    slow = head
    fast = head
    
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow

def sort(head: Node) -> Node:
    # Write your code here...
    if head is None or head.next is None:
        return head
    mid = get_mid(head)
    left = head
    right = mid.next
    mid.next = None
    left = sort(left)
    right = sort(right)
    return merge_sort(left, right)

if __name__=="__main__":
    arr = [6, 3, 4, 8, 2, 9]
    linked_list = construct(arr)
    ans = sort(linked_list)
    print(print_linked_list(ans))
