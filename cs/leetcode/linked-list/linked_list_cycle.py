"""
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents
the position (0-indexed) in the linked list where tail connects to. If pos is -1, then
there is no cycle in the linked list.



Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Follow up:

Can you solve it using O(1) (i.e. constant) memory?
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def solution(head: ListNode) -> bool:
    """
    time complexity: O(n)
    space complexity: O(n)
    """
    addresses = set()
    current = head

    while current:
        address = id(current)

        if address in addresses:
            return True

        addresses.add(address)
        current = current.next

    return False


def solution_constant_memory(head: ListNode) -> bool:
    """
    Avoir deux pointeurs, l'un qui avance une case par une case, l'autre deux  par deux.
    S'il y a un cycle, les deux pointeurs vont finir par se rencontrer.

    time complexity: O(n)
    space complexity: O(1)
    """
    if not head:
        return False

    fast = head.next
    slow = head

    while fast and slow and fast != slow:
        slow = slow.next
        fast = fast.next

        if fast:
            fast = fast.next

    if not fast:
        return False

    return True


def get_input_1():
    elem0 = ListNode(3)
    elem1 = ListNode(2)
    elem2 = ListNode(0)
    elem3 = ListNode(-4)

    elem0.next = elem1
    elem1.next = elem2
    elem2.next = elem3
    elem3.next = elem1

    return elem0


def get_input_2():
    elem0 = ListNode(1)
    elem1 = ListNode(2)

    elem0.next = elem1
    elem1.next = elem0

    return elem0


def get_input_3():
    return ListNode(1)


def get_input_4():
    elem0 = ListNode(1)
    elem0.next = elem0
    return elem0


print("Simple solutions:")
print(f"- solution 1: {solution(get_input_1())}")
print(f"- solution 2: {solution(get_input_2())}")
print(f"- solution 3: {solution(get_input_3())}")
print(f"- solution 4: {solution(get_input_4())}")

print("\n")

print("Constant memory solutions:")
print(f"- solution 1: {solution_constant_memory(get_input_1())}")
print(f"- solution 2: {solution_constant_memory(get_input_2())}")
print(f"- solution 3: {solution_constant_memory(get_input_3())}")
print(f"- solution 4: {solution_constant_memory(get_input_4())}")
