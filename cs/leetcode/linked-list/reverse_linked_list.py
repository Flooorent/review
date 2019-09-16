"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def print_linked_list(head: ListNode) -> None:
    values = []
    current = head

    while current:
        values.append(current.val)
        current = current.next

    print(' -> '.join(map(str, values)))


def create_linked_list():
    elem0 = ListNode(10)
    elem1 = ListNode(20)
    elem2 = ListNode(30)

    elem1.next = elem2
    elem0.next = elem1

    return elem0


def iterative_solution(head: ListNode) -> ListNode:
    previous = None
    current = head

    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    return previous


def recursive_solution(head: ListNode) -> ListNode:
    def rec(head: ListNode, prev: ListNode) -> ListNode:
        if not head:
            return prev

        next_node = head.next
        head.next = prev

        return rec(next_node, head)

    return rec(head, None)


input0 = create_linked_list()
print_linked_list(input0)

output0 = iterative_solution(input0)
print_linked_list(output0)

input1 = create_linked_list()
print_linked_list(input1)

output1 = recursive_solution(input1)
print_linked_list(output1)
