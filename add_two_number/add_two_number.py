from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer_first = answer_last = None
        overflow, value = 0, 0
        while l1 is not None or l2 is not None:
            a = l1.val if l1 is not None else 0
            b = l2.val if l2 is not None else 0
            sum = a + b + overflow
            overflow, value = divmod(sum ,10)
            new_node = ListNode(value)
            if answer_first is None:
                answer_first = answer_last = new_node
            else:
                answer_last.next = new_node
                answer_last = new_node
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        if overflow > 0:
            new_node = ListNode(overflow)
            answer_last.next = new_node
            answer_last = new_node
        return answer_first