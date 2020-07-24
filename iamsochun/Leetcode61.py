# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return head
        first = second = head
        num = 1
        i = 1
        while i <= k:
            if first.next is not None:
                first = first.next
                num = num+1
            else:
                k = k % num
                i = 0
                first = head
            i = i+1
        while first.next is not None:
            first = first.next
            second = second.next
        if second.next is not None:
            first.next = head
            head = second.next
            second.next = None
        return head