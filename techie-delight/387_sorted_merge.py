'''

Given k sorted singly-linked lists of integers, merge them into a single list in increasing order, and return it.

Input: [
	1 —> 5 —> 7 —> None,
	2 —> 3 —> 6 —> 9 —> None,
	4 —> 8 —> 10 —> None
]

Output: 1 —> 2 —> 3 —> 4 —> 5 —> 6 —> 7 —> 8 —> 9 —> 10 —> None

'''

import heapq

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

def sorted_merge(lists: List[Node]) -> Node:
    sorted_list = []
    heap = []
    heapq.heapify(heap)
    for i in range(len(lists)):
        element_data = lists[i].data
        element_head = lists[i]
        list_index = i
        heapq.heappush(heap, (element_data, element_head, list_index))

    while len(heap) > 0:
        element_data, element_head, list_index = heapq.heappop(heap)
        sorted_list.append(element_data)
        
        # if element_head next exists, then push that to max heap
        if element_head.next:
            next_element_head = element_head.next
            next_element_data = next_element_head.data
            heapq.heappush(heap, (next_element_data, next_element_head, list_index))
    
    # construct linked list from list
    head = None
    for i in range(len(sorted_list) - 1, -1, -1):
        element_data = sorted_list[i]
        this_node = Node(data=element_data)
        this_node.next = head
        head = this_node
    return head

if __name__=="__main__":
    input = [
        construct([1, 5, 7]),
        construct([2, 3, 6, 9]),
        construct([4, 8, 10])
    ]
    ans = sorted_merge(input)
    print(print_linked_list(ans))
